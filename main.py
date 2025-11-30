
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory, QTableWidgetItem, QHeaderView, QMessageBox, QListWidgetItem, QCalendarWidget, QMenu, QToolButton
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QBrush, QGuiApplication

# system modules
import os
import sys
import pandas as pd
import datetime
import webbrowser
import shutil
import configparser

# own modules
from mainwindow import Ui_MainWindow
import settings
import gui_actions
import monitor
import map
import add_venue
import add_show
import calc
import exports


# pandas options
pd.set_option('display.max_columns', 22)
#pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 2000)


# In PyCharm:
# in Run Configuration, Run Before Launch, add External Tool
# Command: pyside6-uic
# Arguments: mainwindow.ui -o mainwindow.py
# Folder: $ProjectFileDir$

# Compile resources:
# Command: pyside6-rcc
# Arguments: images.qrc -o images_rc.py

# Pycharm navigate back: ctrl+alt+pageup

# Pyinstaller:
# pyinstaller -w -n TourManager --icon=icon.ico --hidden-import=tabulate --hidden-import=pyqtdarktheme-fork main.py

# Dependencies:
# PySide6 pandas folium ics tabulate humanize pyqtdarktheme-fork



VERSION = "1.0.0"
DATE = ("2025-11-30")

DB_SHOWS = "shows.csv"
DB_VENUES = "venues.csv"
CONFIG_FILE = "config.ini"
LOCK_FILE = "LOCKED"


STATUS = ["ALL", "UPCOMING", "PLAYED", "WORK IN PROGRESS", "WAITING FOR FEE", "CANCELLED"]
SHOW_STATUS = STATUS.copy()
SHOW_STATUS.pop(0) # remove "ALL"

VENUE_FILTERS = ["ALL", "EXISTING", "WITH SHOWS", "WITHOUT SHOWS", "RATINGS", "EVENTS (ALL)", "EVENTS (EXISTING)"]
VENUE_RATINGS = ["", "*", "* *", "* * *", "* * * *", "* * * * *"]





class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print(QStyleFactory.keys()) # qt styles
        self.setWindowTitle("TourManager " + VERSION)

        # load config
        self.load_config()

        # check lock
        self.check_lock()

        # auto backup DBs
        self.backup_db("start")

        # notes flag
        self.notes_opened = False

        # populate status filter and show status comboboxes
        self.ui.cb_show_status_filter.addItems(STATUS)
        self.ui.cb_show_status.addItems(SHOW_STATUS)

        # populate venue filters combobox and rating combobox
        self.ui.cb_venue_filter.addItems(VENUE_FILTERS)
        self.ui.cb_venue_rating.addItems(VENUE_RATINGS)


        # load DATABASES and populate lists
        self.load_databases()
        self.populate_show_list(self.df_shows_in_list)
        self.populate_venue_list(self.df_venues_sorted)

        # flags
        self.show_search_flag = False
        self.config_needs_restart = False

        # monitor
        self.ui.cb_monitor.addItems(monitor.CB_MONITOR_ITEMS)
        monitor.fill_monitor(self)

        # disable folder button
        self.ui.bt_show_folder.setEnabled(False)

        # set is_event checkbox
        gui_actions.check_venue_is_event(self.ui)

        # disable mouse wheel for tag cb fields
        self.ui.field_venue_cb_tags.wheelEvent = lambda event: None
        self.ui.field_show_cb_tags.wheelEvent = lambda event: None

        # generate tag lists (show need to be selected)
        self.generate_shows_tag_list()
        self.generate_venues_tag_list()


        #set special values to dateedit (needed to show empty dateedit widgets - it replaces invalid dates)
        self.ui.field_show_dateedit.setSpecialValueText(" ")
        self.ui.field_venue_start_dateedit.setSpecialValueText(" ")
        self.ui.field_venue_end_dateedit.setSpecialValueText(" ")

        # set calendar widgets with week numbers and monday as first day of week
        self.calendar_show = QCalendarWidget(self)
        self.calendar_show.setFirstDayOfWeek(Qt.Monday)
        self.calendar_show.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
        self.ui.field_show_dateedit.setCalendarWidget(self.calendar_show)

        self.calendar_event_start = QCalendarWidget(self)
        self.calendar_event_start.setFirstDayOfWeek(Qt.Monday)
        self.calendar_event_start.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
        self.ui.field_venue_start_dateedit.setCalendarWidget(self.calendar_event_start)

        self.calendar_event_end = QCalendarWidget(self)
        self.calendar_event_end.setFirstDayOfWeek(Qt.Monday)
        self.calendar_event_end.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
        self.ui.field_venue_end_dateedit.setCalendarWidget(self.calendar_event_end)


        # setup search history
        self.search_shows_history = []
        self.search_venues_history = []


        # pre-defined variables
        self.search_text = ""
        self.tmp_tags = ""


        # select a show and setup everything
        items = self.ui.list_show.findItems(self.config_selected_show, Qt.MatchContains)
        if self.config_selected_show != "" and self.config_start_with_selected_show == "1" and len(items) > 0: # select previously selected show (by name, because showID can change)
            self.ui.list_show.setCurrentItem(items[0])
        else:
            #self.ui.list_show.setCurrentRow(0) # select first show
            self.ui.list_show.setCurrentRow(self.ui.list_show.count()-1) # select last show in list
        self.select_show()
        self.select_venue()
        gui_actions.check_venue_is_event(self.ui)
        self.select_venue() # needed again after gui_actions.check_venue_is_event
        self.ui.list_show.setFocus()

        # hide unused widgets
        self.ui.my_button.hide()
        self.ui.table_show.hide()
        self.ui.field_show_show_id.hide()
        self.ui.field_show_venue_id.hide()
        self.ui.field_venue_venue_id.hide()





        # SIGNALS
        self.ui.my_button.clicked.connect(self.open_settings)

        self.ui.cb_search_shows.editTextChanged.connect(self.on_search_shows)
        self.ui.cb_search_shows.lineEdit().editingFinished.connect(lambda: self.add_to_search_history("shows"))  # get finished signal from underlying linedit
        self.ui.cb_search_shows.findChild(QToolButton).pressed.connect(lambda: self.add_to_search_history("shows"))  # -> get signal from clearbutton pressed (because clicked is sent after emptying)

        self.ui.cb_search_venues.editTextChanged.connect(self.on_search_venues)
        self.ui.cb_search_venues.lineEdit().editingFinished.connect(lambda: self.add_to_search_history("venues"))
        self.ui.cb_search_venues.findChild(QToolButton).pressed.connect(lambda: self.add_to_search_history("venues"))


        self.ui.bt_assign_venue_to_show.clicked.connect(lambda: gui_actions.assign_venue_to_show(self.ui, self.selected_venue))
        self.ui.list_venue.doubleClicked.connect(lambda: gui_actions.assign_venue_to_show(self.ui, self.selected_venue))

        self.ui.cb_show_status_filter.activated.connect(self.on_search_shows)
        self.ui.cb_venue_filter.activated.connect(self.on_search_venues)

        self.ui.list_show.currentRowChanged.connect(self.select_show)
        self.ui.list_venue.currentRowChanged.connect(self.select_venue)

        self.ui.field_show_dateedit.dateChanged.connect(lambda qdate: self.ui.lb_show_weekday.setText(gui_actions.get_weekday_name(qdate)))

        self.ui.bt_show_folder.clicked.connect(lambda: gui_actions.open_or_create_show_folder(self.ui, self.selected_show, self.df_venues, self.config_workdir))

        self.ui.field_show_fee.valueChanged.connect(lambda: gui_actions.update_show_fee_sum(self.ui))
        self.ui.field_show_travel_costs.valueChanged.connect(lambda: gui_actions.update_show_fee_sum(self.ui))

        self.ui.bt_save_show.clicked.connect(self.on_save_show)
        self.ui.bt_delete_show.clicked.connect(self.delete_show)
        self.ui.bt_new_show.clicked.connect(lambda: self.on_new_show("New"))
        self.ui.bt_duplicate_show.clicked.connect(lambda: self.on_new_show("Duplicate"))

        self.ui.field_venue_start_dateedit.dateChanged.connect(lambda: gui_actions.start_date_changed(self.ui))
        self.ui.field_venue_end_dateedit.dateChanged.connect(lambda: gui_actions.end_date_changed(self.ui))

        self.ui.bt_save_venue.clicked.connect(self.on_save_venue)
        self.ui.bt_delete_venue.clicked.connect(self.delete_venue)
        self.ui.bt_new_venue.clicked.connect(self.on_new_venue)

        self.ui.bt_venue_search_shows.clicked.connect(self.on_venue_search_show)


        self.ui.field_venue_city.activated.connect(lambda: gui_actions.on_select_city(self))

        self.ui.bt_venue_locate.clicked.connect(self.on_venue_locate)
        self.ui.bt_venue_route.clicked.connect(self.on_venue_route)
        self.ui.bt_venue_locate_geocoordinates.clicked.connect(self.on_venue_locate_geo_coordinates)
        self.ui.field_checkbox_venue_is_event.stateChanged.connect(lambda: gui_actions.check_venue_is_event(self.ui))
        self.ui.bt_website.clicked.connect(self.on_show_website)

        self.ui.cb_monitor.activated.connect(lambda: monitor.fill_monitor(self))
        self.ui.bt_map.clicked.connect(self.open_map)
        self.ui.bt_calculator.clicked.connect(self.open_calculator)

        self.ui.field_show_cb_tags.textActivated.connect(lambda sel: self.add_tag(sel, self.ui.field_show_cb_tags))
        self.ui.field_show_cb_tags.highlighted.connect(lambda sel: self.save_tmp_tags_from_field(sel, self.ui.field_show_cb_tags))
        self.ui.field_venue_cb_tags.textActivated.connect(lambda sel: self.add_tag(sel, self.ui.field_venue_cb_tags))
        self.ui.field_venue_cb_tags.highlighted.connect(lambda sel: self.save_tmp_tags_from_field(sel, self.ui.field_venue_cb_tags))




        # MENU signals
        self.ui.actionBackup.triggered.connect(lambda: self.backup_db("dated"))
        self.ui.actionSettings.triggered.connect(self.open_settings)
        self.ui.actionQuit.triggered.connect(app.quit)

        self.ui.actionFuture_Shows.triggered.connect(lambda: exports.export_shows_to_html(self.df_shows, self.df_venues, self.config_workdir, self.ui))
        self.ui.actionCalendars.triggered.connect(lambda: exports.export_all_calendars(self.df_shows, self.df_venues, self.config_workdir, self.ui, SHOW_STATUS))

        self.ui.actionOpen_Working_Folder.triggered.connect(lambda: gui_actions.open_file_or_folder(os.path.abspath(self.config_workdir)))
        self.ui.actionOpen_Show_Folder.triggered.connect(lambda: gui_actions.open_file_or_folder(os.path.join(self.config_workdir, "Shows")))
        self.ui.actionOpen_Backup_Folder.triggered.connect(lambda: gui_actions.open_file_or_folder(os.path.abspath("./Backups")))
        self.ui.actionOpen_Root_Folder.triggered.connect(lambda: gui_actions.open_file_or_folder(os.path.abspath("")))

        self.ui.actionMap.triggered.connect(self.open_map)
        self.ui.actionTravel_Costs_Calculator.triggered.connect(self.open_calculator)

        self.ui.actionAbout.triggered.connect(self.on_about)


        # toolbuttons menus
        self.monitor_menu = QMenu()
        self.monitor_menu.addAction("Copy monitor", lambda: self.copy_monitor_text("full"))
        self.monitor_menu.addAction("Copy selection", lambda: self.copy_monitor_text("selection"))
        self.monitor_menu.addSeparator()
        self.monitor_menu.addAction("Search selection in shows", lambda: self.search_selected_text("shows"))
        self.monitor_menu.addAction("Search selection in venues", lambda: self.search_selected_text("venues"))
        self.monitor_menu.addAction("Search selection in both", lambda: self.search_selected_text("both"))
        self.ui.bt_monitor_menu.setMenu(self.monitor_menu)
        #self.monitor_menu.aboutToShow.connect(self.test) use this to enable/disable menu entries



        # apply histories (needs to be set after signals)
        self.search_shows_history = eval(self.config_search_shows_history) if self.config_search_shows_history != "" else []
        self.add_to_search_history("shows") # setup everything
        self.search_venues_history = eval(self.config_search_venues_history) if self.config_search_venues_history != "" else []
        self.add_to_search_history("venues") # setup everything







    # ------------------------------------------ CHECKS, CONFIG & DATABASES ------------------------------------------

    def load_config(self):
        # create object
        self.config = configparser.ConfigParser(comment_prefixes="#", inline_comment_prefixes="#")

        # generate config if config file doesn't exist
        if os.path.exists(CONFIG_FILE) == False:
            self.config["defaults"] = {"homebase_city": "Homebase City (Dummy)",
                                       "homebase_geocoordinates": "0.0, 0.0",
                                       "artist": "My Artist",
                                       "currency": "EUR",
                                       "distance_unit": "km",
                                       "travel_unit_price": "0.30"}
            self.config["paths"] = {"working_directory": "."}
            self.config["settings"] = {"auto_export_shows": "0",
                                       "auto_export_calendars": "0",
                                       "map_provider": "osm",
                                       "calc_text_decimal_separator": ",",
                                       "custom_links": '[(r"TourManager Web", r"https://github.com/sonejostudios/TourManager"), (r"|",r""), ("App Notes", r"Notes.txt"), ("App Folder", r".")]',
                                       "selected_show": "",
                                       "start_with_selected_show": "1"}
            self.config["gui"] = {"theme": "",
                                  "font_size": "10",
                                  "field_area_width": "430",
                                  "save_window_size": "1",
                                  "window_width": "1700",
                                  "window_height": "1000",
                                  "start_maximized": "0"}
            self.config["histories"] = {"search_shows_history": "",
                                        "search_venues_history": ""}


            with open(CONFIG_FILE, "w", encoding='utf-8') as configfile:
                self.config.write(configfile)

            QMessageBox.warning(self, "TourManager Configuration",
                                "It is the first time you are starting TourManager!\n\n"
                                "1. A configuration file (config.ini) was generated.\n\n"
                                "2. You must copy shows.csv and venues.csv into the working folder. Otherwise, TourManager will not start.\n\n"
                                "3. When all this is setup, please start TourManager again!",
                                QMessageBox.Ok, QMessageBox.Ok)
            sys.exit()


        # read config and get variables
        self.config.read(CONFIG_FILE)

        self.config_homebase_city = self.config.get("defaults", "homebase_city")
        self.config_homebase_geocoordinates = self.config.get("defaults", "homebase_geocoordinates")
        self.config_artist = self.config.get("defaults", "artist")
        self.config_currency = self.config.get("defaults", "currency")
        self.config_distance_unit = self.config.get("defaults", "distance_unit")
        self.config_travel_unit_price = float(self.config.get("defaults", "travel_unit_price"))

        self.config_workdir = self.config.get("paths", "working_directory")
        print("Workdir:", self.config_workdir)

        self.config_auto_export_shows = self.config.get("settings", "auto_export_shows")
        self.config_auto_export_calendars = self.config.get("settings", "auto_export_calendars")
        self.config_map_provider = self.config.get("settings", "map_provider")
        self.config_calc_dec_sep = self.config.get("settings", "calc_text_decimal_separator")
        self.config_custom_links = self.config.get("settings", "custom_links")
        self.config_selected_show = self.config.get("settings", "selected_show")
        self.config_start_with_selected_show = self.config.get("settings", "start_with_selected_show")

        self.config_theme = self.config.get("gui", "theme")
        self.config_font_size = self.config.get("gui", "font_size")
        self.config_field_area_width = self.config.get("gui", "field_area_width")
        self.config_save_window_size = self.config.get("gui", "save_window_size")
        self.config_window_width = self.config.get("gui", "window_width")
        self.config_window_height = self.config.get("gui", "window_height")
        self.config_start_maximizied = self.config.get("gui", "start_maximized")

        self.config_search_shows_history = self.config.get("histories", "search_shows_history")
        self.config_search_venues_history = self.config.get("histories", "search_venues_history")



        # check if working folder exists, if not ask user to select it
        if os.path.exists(self.config_workdir) == False:
            QMessageBox.warning(self, "TourManager Error",
                                "The working folder was not found.\nPlease select an existing working folder containing the databases (shows.csv and venues.csv).",
                                QMessageBox.Ok, QMessageBox.Ok)
            self.open_settings(1) # open settings tab "paths"



        # APPLY CONFIG
        # homebase
        self.ui.lb_homebase.setText(self.config_homebase_city)
        homebase_text = "Homebase:\n"+self.config_homebase_city + "\n" + self.config_homebase_geocoordinates
        self.ui.lb_homebase.setToolTip(homebase_text)
        self.ui.bt_venue_route.setToolTip("Show directions from " + self.config_homebase_city + " to this address on the web")


        # add custom links to menu (or hide menu item if no custome links are provided)
        if self.config_custom_links != "":
            #print("Add Custom Links:")
            self.ui.menuCustom_Links.clear() # clear menu first to avoid duplicates on config reload
            for item in eval(self.config_custom_links):
                #print(item)
                if item[0] == "|":
                    self.ui.menuCustom_Links.addSeparator()
                else:
                    action = self.ui.menuCustom_Links.addAction("%s" % item[0])
                    action.triggered.connect(lambda chk, item=item: self.open_custom_link(item[1]))
        else:
            self.ui.menuCustom_Links.deleteLater()



        # apply pyqtdarktheme if installed and configured, otherwise Qt-Fusion (follows OS colors) is used (theme = empty)
        if self.config_theme in ["dark", "light", "auto"]:
            # reset buttons min height to 0 because qdarktheme ignores combobox min height set in wainwindow.ui -> also needed: apply additional_qss to themes
            self.ui.bt_map.setMinimumHeight(0)
            self.ui.bt_calculator.setMinimumHeight(0)

            # import the theme here to prevent crashing if pyqtdarktheme is not installed
            import qdarktheme

            if self.config_theme == "dark":
                qdarktheme.setup_theme(custom_colors={"input.background": "#1C1D1F"}, additional_qss="QComboBox { min-height: 1em; padding: 3px 4px; }") # 2-> dark
            elif self.config_theme == "light":
                qdarktheme.setup_theme("light", additional_qss="QComboBox { min-height: 1em; padding: 3px 4px; }") # 3-> light
            else:
                qdarktheme.setup_theme("auto", additional_qss="QComboBox { min-height: 1em; padding: 3px 4px; }") # 1-> auto




        # apply font size, field area with and start maximized
        # set global font size (empty = 10)
        if self.config_font_size != "":
            self.setStyleSheet(u"font: " + self.config_font_size + "pt;")

        # set field width (empty = 430)
        if self.config_field_area_width != "":
            field_width = int(self.config_field_area_width)
            self.ui.shows_panel.setFixedWidth(field_width)
            self.ui.venues_panel.setFixedWidth(field_width)


        # window size or maximized
        if self.config_start_maximizied == "1":
            self.showMaximized()

        elif self.config_window_width != "" and self.config_window_height != "":
            #self.setMinimumSize(200,100) # uncomment to allow smaller sizes
            self.resize(int(self.config_window_width), int(self.config_window_height))


        # some important gui tuning (not in config)
        gui_actions.setup_search_comboboxes(self.ui.cb_search_shows, self.ui.cb_search_venues)




    def check_lock(self): # check if app is locked or not, if yes shut it down, if no create lock file
        print("check lock")
        lock_file = os.path.join(self.config_workdir, LOCK_FILE)
        if os.path.exists(lock_file):
            print("App is LOCKED")
            QMessageBox.warning(self, "TourManager Error", "TourManager is locked because another user is using it right now.\nPlease wait util it is unlocked to start it again.", QMessageBox.Ok, QMessageBox.Ok)
            sys.exit()
        else:
            if os.path.exists(self.config_workdir) == False or os.path.exists(os.path.join(self.config_workdir, DB_SHOWS)) == False or os.path.exists(os.path.join(self.config_workdir, DB_SHOWS)) == False:
                QMessageBox.warning(self, "TourManager Error",
                                    "The working folder doesn't exist or the databases are missing!\n\nPlease make sure the databases (shows.csv and venues.csv) are inside the working folder.", QMessageBox.Ok, QMessageBox.Ok)
                sys.exit()  # exit app if workdir not found

            else:
                with open(lock_file, 'w') as file:
                    file.write(str(datetime.datetime.now()) + '\n\nThis file locks TourManager to prevent multi-user usage.\n'
                               'It will be deleted as soon as the app is closed.')





    def backup_db(self, how):
        print("DB Backups created")
        os.makedirs("./Backups/", exist_ok=True)

        if how == "start": # -> is this really needed in final version?
            # make start copy (DEV)
            shutil.copyfile(os.path.join(self.config_workdir, DB_SHOWS), "./Backups/startbak_" + DB_SHOWS)
            shutil.copyfile(os.path.join(self.config_workdir, DB_VENUES), "./Backups/startbak_" + DB_VENUES)

        else:
            # make copy with timestamp (for Backup Menu)
            timestamp = f'{datetime.datetime.now():%Y%m%d_%H%M%S}'
            shutil.copyfile(os.path.join(self.config_workdir, DB_SHOWS), "./Backups/" + timestamp + "_" + DB_SHOWS)
            shutil.copyfile(os.path.join(self.config_workdir, DB_VENUES), "./Backups/" + timestamp + "_" + DB_VENUES)

            self.ui.statusbar.showMessage("Backup of databases created! (" + timestamp + ")", 3000)




    def load_databases(self):
        # load SHOWS.CSV
        df_shows_path = os.path.join(self.config_workdir, DB_SHOWS)
        self.df_shows = pd.read_csv(df_shows_path).fillna("")

        # generate ShowID and set VenueID as int
        self.df_shows["ShowID"] = self.df_shows.index # copy index into column (needed for navigation with qt shows list)
        self.df_shows["VenueID"].astype(int)

        print(self.df_shows)

        # copy df_show to df_show_in_list (= df shown and filtered in show_list)
        self.df_shows_in_list = self.df_shows



        # load VENUES.CSV
        df_venues_path = os.path.join(self.config_workdir, DB_VENUES)
        self.df_venues = pd.read_csv(df_venues_path, index_col="VenueID").fillna("")#.astype(str)
        self.df_venues["VenueRating"].astype(str)

        # sort df_venues
        self.on_search_venues()

        print(self.df_venues)






    # --------------------------------------------- SHOWS ---------------------------------------------

    def populate_show_list(self, df): # show list
        self.ui.list_show.clear()

        for index, row in df.iterrows():
            show_str = str(row["Date"]) + " - " + str(row["City"]) + " - " + str(row["Venue"]) # from df_shows

            # create and add item (grey out cancelled shows)
            item = QListWidgetItem(show_str)
            if str(row["Status"]) == "4": # cancelled
                item.setForeground(QBrush("#888A85"))
            self.ui.list_show.addItem(item)

        # count shows
        self.ui.label_show_amount.setText(str(len(df)))




    def on_search_shows(self): # search shows
        self.show_search_flag = True # -> Flag!

        # get status filter and its id
        state_id = STATUS.index(self.ui.cb_show_status_filter.currentText())
        #print(state_id)

        # filter by state if not "ALL"
        if state_id != 0:
            self.df_shows_state_filtered = self.df_shows[self.df_shows["Status"] == state_id-1].reset_index(drop=True)
        else:
            self.df_shows_state_filtered = self.df_shows



        # filter by keyword
        # search all rows with search entry inside state filtered df
        text = self.ui.cb_search_shows.currentText()
        if text != "":
            # https://stackoverflow.com/questions/38980514/most-concise-way-to-select-rows-where-any-column-contains-a-string-in-pandas-dat
            self.df_shows_in_list = self.df_shows_state_filtered[self.df_shows_state_filtered.apply(lambda r: r.str.contains(text, case=False, regex=False).any(), axis=1)]
            self.df_shows_in_list = self.df_shows_in_list.reset_index(drop=True)
        else:
            self.df_shows_in_list = self.df_shows_state_filtered

        # populate widget list
        self.populate_show_list(self.df_shows_in_list)

        # scroll list to the newest shows
        self.ui.list_show.scrollToBottom()

        # fill monitor (only if notes are not opened)
        if self.notes_opened == False:
            monitor.fill_monitor(self)

        # clear fields
        gui_actions.clear_show_fields(self.ui)

        self.show_search_flag = False # -> Flag!




    def select_show(self):
        print("select show:",self.ui.list_show.selectedItems())

        if self.show_search_flag == False: # prevent multiple runs from signals and error
            # get current row
            row = self.ui.list_show.currentRow()
            #print("row", row)

            if row != -1: # prevent error if no show is selected
                # enable buttons
                self.ui.bt_save_show.setEnabled(True)
                self.ui.bt_delete_show.setEnabled(True)
                self.ui.bt_duplicate_show.setEnabled(True)


                # get show with row = index
                self.selected_show = self.df_shows_in_list.loc[row]
                print(self.selected_show.to_frame().T) # print row horizontally
                #print(self.selected_show)

                # show selected show in table ------------------------------DEV ONLY--------------------------------
                self.show_show_in_table(self.selected_show)

                # get data from show.csv and fill fields
                gui_actions.fill_show_fields(self.ui, self.selected_show, self.df_shows)

                # check if folder exists and enable folder button
                gui_actions.check_show_folder_exists(self.ui, self.selected_show, self.df_venues, self.config_workdir)
                self.ui.bt_show_folder.setEnabled(True)

                # show all venues in list (reset all filters and searches)
                self.ui.cb_search_venues.setCurrentText("")
                self.ui.cb_venue_filter.setCurrentIndex(0)
                self.on_search_venues()


                # IF venueID in df_venue, try to select venue in venue_list (this triggers fill_venue_fields).
                venue_id = self.selected_show["VenueID"]
                show_id = self.selected_show["ShowID"]

                if venue_id in self.df_venues["VenueID"]:
                    # select venue
                    wanted_row = self.df_venues_in_list.loc[self.df_venues_in_list['VenueID'] == venue_id].index[0]
                    self.ui.list_venue.setCurrentRow(wanted_row)

                    # COPY venue name, city and country from df_venues into df_shows - to keep them always updated!
                    self.df_shows.at[show_id, "Venue"] = self.df_venues.loc[venue_id]["VenueName"]
                    self.df_shows.at[show_id, "City"] = self.df_venues.loc[venue_id]["VenueCity"]
                    self.df_shows.at[show_id, "Country"] = self.df_venues.loc[venue_id]["VenueCountry"]



                else:
                    #take venue info from df_shows and add mention as deleted
                    self.ui.list_venue.clearSelection()
                    gui_actions.clear_venue_fields(self.ui)
                    venue_text = str(self.selected_show["City"]) + " - " + str(self.selected_show["Venue"]) + " (DELETED)" # from df_shows
                    self.ui.field_show_venue_text.setText(venue_text)

                    # set venue id in df_shows to -1 (= no venue id because venue was deleted)
                    self.df_shows.at[show_id, "VenueID"] = -1






    def on_new_show(self, how): # new or duplicate show button

        if self.ui.field_venue_venue_id.text() == "" and how == "New":
            QMessageBox.information(self, "Create New Show","You need to select a venue to create a new show.\nPlease select one.")
            return

        # create and open new show dialog
        venue_text = str(self.selected_venue["VenueCity"]) + " - " + str(self.selected_venue["VenueName"])
        wanted_date = self.ui.field_show_dateedit.date() if self.ui.field_show_dateedit.isEnabled() else QDate.currentDate()
        self.add_show_dialog = add_show.AddShowDialog(self, how, wanted_date, venue_text)
        ok = self.add_show_dialog.exec()

        if ok == 1:
            new_date = self.add_show_dialog.on_ok()  # get date from dialog

            # clear fields if button "new show" was clicked
            if how == "New":
                gui_actions.clear_show_fields(self.ui)
                self.ui.field_show_artists.setEditText(self.config_artist)
                self.ui.field_show_currency.setEditText(self.config_currency)
                self.ui.cb_show_status.setCurrentIndex(2) # set status to "work in progress"

                # copy venue id to create new show with selected venue
                wanted_venue_id = self.ui.field_venue_venue_id.text()
                if wanted_venue_id != "":
                    self.ui.field_show_venue_id.setText(wanted_venue_id)


            # save show string for UPCOMING SELECTION
            if len(self.ui.list_venue.selectedItems()) > 0:
                show_str = str(new_date) + " - " + self.selected_venue["VenueCity"] + " - " + self.selected_venue["VenueName"]
            else:
                show_str = str(new_date) + " - " + " - "

            # create new show
            self.ui.field_show_dateedit.setDate(QDate.fromString(new_date, "yyyy-MM-dd"))
            last_show_id = self.df_shows["ShowID"].iloc[-1]
            new_show_id = last_show_id + 1
            self.save_show(new_show_id)

            # select new show (UPCOMING SELECTION)
            item = self.ui.list_show.findItems(show_str, Qt.MatchContains)  # returns list of items which matches with show_str
            if len(item) > 0:
                self.ui.list_show.setCurrentItem(item[0])




    def on_save_show(self): # save show button
        self.save_show(self.selected_show["ShowID"])

        # update tag list
        self.generate_shows_tag_list()

        # notify
        self.ui.statusbar.showMessage("Current Show saved!", 3000)



    def save_show(self, show_id): # save show into df_shows and into file
        print("save show")

        # check if venue exists and set "copy_venue_info" flag
        copy_venue_info = True if self.selected_show["VenueID"] in self.df_venues["VenueID"] else False

        # update df_shows
        gui_actions.update_df_shows(self.ui, self.df_shows, show_id, copy_venue_info, self.df_venues)

        # SORT df_shows (by date AND city to avoid bugs with duplicate dates) -> maybe use showtime instead
        self.df_shows = self.df_shows.sort_values(by=["Date", "City"], ascending=True).reset_index(drop=True)
        self.df_shows["ShowID"] = self.df_shows.index
        self.df_shows["VenueID"] = self.df_shows["VenueID"].astype(int)
        self.df_shows["Status"] = self.df_shows["Status"].astype(int)

        # reload search and reselect show - needed to update everything
        self.reload_reselect_showlist()

        # save file
        self.save_df_shows_to_file()





    def save_df_shows_to_file(self): # save df_shows into shows.csv
        # save df_shows to file
        df_show_to_file = self.df_shows.drop("ShowID", axis=1) # drop ShowID column (used only to navigate with qt show list)

        df_shows_path = os.path.join(self.config_workdir, DB_SHOWS)
        df_show_to_file.to_csv(df_shows_path, index=False) # SAVE TO DB_SHOWS FILE
        #print(df_show_to_file)



    def delete_show(self):
        print("delete show")

        # exit if df_show has only one item
        if len(self.df_shows) <= 1:
            QMessageBox.information(self, "Database Error", "The Show Database can't be empty.\nPlease create a new show before deleting this one.")
            return

        # delete dialog
        show_txt = self.ui.list_show.currentItem().text()
        reply = QMessageBox.warning(self, "Delete Show", "Do you really want to delete this show?" + "\n\n" + show_txt, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            show_id = self.selected_show["ShowID"]

            # delete show at id and reset index
            self.df_shows = self.df_shows.drop(show_id).reset_index(drop=True)

            # re-generate ShowID and reload search (needed to update everything)
            self.df_shows["ShowID"] = self.df_shows.index
            self.on_search_shows()

            # save file
            self.save_df_shows_to_file()




    def reload_reselect_showlist(self):
        # reload search and reselect show (needs to be done to reload all filtered df copies and update the show list)
        row = self.ui.list_show.currentRow()
        self.on_search_shows()
        self.ui.list_show.setCurrentRow(row)





# --------------------------------------------- VENUES ---------------------------------------------

    def populate_venue_list(self, df): # venue list
        self.ui.list_venue.clear()

        # get filter id
        filter_id = VENUE_FILTERS.index(self.ui.cb_venue_filter.currentText())

        # set item strings
        for index, row in df.iterrows():
            if filter_id in [0, 1, 2, 3]: # ALL, EXISTING, WITH SHOWS, NO SHOWS
                show_str = str(row["VenueCountry"]) + " - " + str(row["VenueCity"]) + " - " + str(row["VenueName"])
                # add date in parentheses
                if bool(row["VenueIsEvent"]) == True:
                    show_str += " (" + str(row["VenueStartDate"]) + ")"

            elif filter_id == 4: # RATINGS
                rating = int(row["VenueRating"]) if row["VenueRating"] != "" else 0
                show_str = str(VENUE_RATINGS[rating]) + " - " + str(row["VenueCountry"]) + " - " + str(row["VenueCity"]) + " - " + str(row["VenueName"])
                if bool(row["VenueIsEvent"]) == True:
                    show_str += " (" + str(row["VenueStartDate"]) + ")"

            else: # EVENTS and EXISTING EVENTS
                show_str = str(row["VenueStartDate"]) + " - " + str(row["VenueCountry"]) + " - " + str(row["VenueCity"]) + " - " + str(row["VenueName"])


            # create and add item (grey out discontinueds)
            item = QListWidgetItem(show_str)
            if bool(row["VenueIsDiscontinued"]) == True:
                item.setForeground(QBrush("#888A85"))
            self.ui.list_venue.addItem(item)


        # count venues
        self.ui.label_venue_amount.setText(str(len(df)))





    def on_search_venues(self): # search venues
        # clear selection
        self.ui.list_venue.clearSelection()

        # copy index to VenueID
        self.df_venues["VenueID"] = self.df_venues.index


        # get filter id
        filter_id = VENUE_FILTERS.index(self.ui.cb_venue_filter.currentText())

        # apply filters
        if filter_id == 0: # ALL
            self.df_venues_sorted = self.df_venues.sort_values(["VenueCountry", "VenueCity", "VenueName"], key=lambda col: col.str.lower()) # ignore case


        elif filter_id == 1: # EXISTING ONLY
            self.df_venues_sorted = self.df_venues.loc[self.df_venues['VenueIsDiscontinued'] == False]
            self.df_venues_sorted = self.df_venues_sorted.sort_values(["VenueCountry", "VenueCity", "VenueName"], key=lambda col: col.str.lower())


        elif filter_id == 2: # WITH SHOWS
            self.df_venues_sorted = self.df_venues.loc[self.df_venues["VenueID"].isin(self.df_shows["VenueID"])] # all which are in df_shows
            self.df_venues_sorted = self.df_venues_sorted.sort_values(["VenueCountry", "VenueCity", "VenueName"], key=lambda col: col.str.lower())

        elif filter_id == 3: # WITHOUT SHOWS
            self.df_venues_sorted = self.df_venues.loc[~self.df_venues["VenueID"].isin(self.df_shows["VenueID"])] # all which are NOT in df_shows
            self.df_venues_sorted = self.df_venues_sorted.sort_values(["VenueCountry", "VenueCity", "VenueName"], key=lambda col: col.str.lower())

        elif filter_id == 4:  # RATINGS
            self.df_venues_sorted = self.df_venues
            self.df_venues_sorted = self.df_venues_sorted.sort_values(["VenueRating", "VenueCountry", "VenueCity", "VenueName"])
            #print(self.df_venues_sorted)

        elif filter_id == 5: # EVENTS ONLY
            self.df_venues_sorted = self.df_venues.loc[self.df_venues['VenueIsEvent'] == True]
            self.df_venues_sorted = self.df_venues_sorted.sort_values(["VenueStartDate", "VenueCountry", "VenueCity", "VenueName"], key=lambda col: col.str.lower())

        elif filter_id == 6: # EXISTING EVENTS ONLY
            self.df_venues_sorted = self.df_venues.loc[(self.df_venues['VenueIsEvent'] == True) & (self.df_venues['VenueIsDiscontinued'] == False)]
            self.df_venues_sorted = self.df_venues_sorted.sort_values(["VenueStartDate", "VenueCountry", "VenueCity", "VenueName"], key=lambda col: col.str.lower())



        # reset index needed
        self.df_venues_in_list = self.df_venues_sorted.reset_index(drop=True)


        # filter by keyword
        # search all rows with search entry inside state filtered df
        text = self.ui.cb_search_venues.currentText()
        if text != "":
            self.df_venues_in_list = self.df_venues_sorted[self.df_venues_sorted.apply(lambda r: r.str.contains(text, case=False, regex=False).any(), axis=1)]
            self.df_venues_in_list = self.df_venues_in_list.reset_index(drop=True)
        else:
            self.df_venues_in_list = self.df_venues_sorted.reset_index(drop=True)

        # populate widget list
        self.populate_venue_list(self.df_venues_in_list)

        # fill monitor (only if notes are not opened)
        if self.notes_opened == False:
            monitor.fill_monitor(self)

        # clear venues fields
        gui_actions.clear_venue_fields(self.ui)

        # disable venue assign button
        self.ui.bt_assign_venue_to_show.setEnabled(False)

        #print(self.df_venues_in_list)






    def select_venue(self):
        # enable buttons
        self.ui.bt_save_venue.setEnabled(True)
        self.ui.bt_delete_venue.setEnabled(True)

        # get current row
        row = self.ui.list_venue.currentRow()

        if row != -1 and row < len(self.df_venues_in_list): # prevent errors from signal self.ui.list_venue.currentRowChanged
            # get venue id with row = index
            self.selected_venue = self.df_venues_in_list.loc[row]
            venue_id = self.selected_venue["VenueID"]

            # fill venue fields if VenueID in venues.csv
            if venue_id in self.df_venues["VenueID"]:
                # print(self.df_venues.loc[venue_id].to_frame().T)
                gui_actions.fill_venue_fields(self.ui, self.df_venues, venue_id)

                # enable venue assign button
                self.ui.bt_assign_venue_to_show.setEnabled(True)




    def on_new_venue(self): # new venue buttons
        self.add_venue_dialog = add_venue.AddVenueDialog(self, self.ui.field_venue_city.currentText(), self.ui.field_venue_country.currentText())
        ok = self.add_venue_dialog.exec()
        if ok == 1:
            venue_name, venue_city, venue_country, new_show = self.add_venue_dialog.on_ok() # get values from dialog

            # clear fields
            gui_actions.clear_venue_fields(self.ui)

            # fill fields from dialog
            self.ui.field_venue_name.setText(venue_name)
            self.ui.field_venue_city.setCurrentText(venue_city)
            self.ui.field_venue_country.setCurrentText(venue_country)

            # create new venue
            last_item_index = self.df_venues.index[-1]  # take last row's index
            new_venue_id = last_item_index + 1
            self.save_venue(new_venue_id)

            # select it in venue list
            wanted_row = self.df_venues_in_list.loc[self.df_venues_in_list['VenueID'] == new_venue_id].index[0]
            self.ui.list_venue.setCurrentRow(wanted_row)

            # trigger new show dialog if wanted
            if new_show == True:
                self.on_new_show("New")




    def on_save_venue(self): # save venue button
        venue_id = int(self.ui.field_venue_venue_id.text())
        self.save_venue(venue_id)

        # update tag list
        self.generate_venues_tag_list()

        # notify
        self.ui.statusbar.showMessage("Current Venue saved!", 3000)



    def save_venue(self, venue_id): # save values to df_venues and into file
        # copy fields into df_venues
        gui_actions.update_df_venues(self.ui, self.df_venues, venue_id)

        # reload search and reselect venue - needed to update everything
        self.reload_reselect_venuelist()

        # save df_venues to file
        self.save_df_venues_to_file()




    def save_df_venues_to_file(self):  # save df_venues into venues.csv
        df_venues_to_file = self.df_venues
        print(df_venues_to_file)

        df_venues_path = os.path.join(self.config_workdir, DB_VENUES)
        df_venues_to_file.to_csv(df_venues_path, index=False) # SAVE TO VENUES FILE



    def delete_venue(self):
        print("delete venue")

        # exit if df_show has only one item
        if len(self.df_venues) <= 1:
            QMessageBox.information(self, "Database Error", "The Venue Database can't be empty.\nPlease create a new venue before deleting this one.")
            return

        # delete dialog
        venue_txt = self.ui.list_venue.currentItem().text()
        reply = QMessageBox.warning(self, "Delete Venue", "Do you really want to delete this venue?" + "\n\n" + venue_txt, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            venue_id = self.selected_venue["VenueID"]

            # delete venue at id (without index reset!)
            self.df_venues = self.df_venues.drop(venue_id)

            # reload search (needed to update everything)
            self.on_search_venues()

            # reselect show to update show fields
            self.select_show()

            # save file
            self.save_df_venues_to_file()



    def reload_reselect_venuelist(self):
        # reload search and reselect show (needs to be done to reload all filtered df copies and update the show list)
        row = self.ui.list_venue.currentRow()
        self.on_search_venues()
        self.ui.list_venue.setCurrentRow(row)





# --------------------------------------------- TAGS ---------------------------------------------
    def generate_shows_tag_list(self):
        field_text = self.ui.field_show_cb_tags.currentText()
        self.ui.field_show_cb_tags.clear()
        shows_taglist = self.generate_tag_list(self.df_shows["Tags"])
        self.ui.field_show_cb_tags.addItems(shows_taglist)
        self.ui.field_show_cb_tags.setCurrentText(field_text) # needs to be re-set because of cb.clear()

    def generate_venues_tag_list(self):
        field_text = self.ui.field_venue_cb_tags.currentText()
        self.ui.field_venue_cb_tags.clear()
        venues_taglist = self.generate_tag_list(self.df_venues["VenueTags"])
        self.ui.field_venue_cb_tags.addItems(venues_taglist)
        self.ui.field_venue_cb_tags.setCurrentText(field_text) # needs to be re-set because of cb.clear()


    def generate_tag_list(self, df_tags_serie): # generate final tag list out of df serie
        tags_set = set(df_tags_serie.to_list()) # remove duplicates
        tags_listoflist = [i.split(" ") for i in tags_set] # split items with many tags
        tags_flat_list = [x for xs in tags_listoflist for x in xs] # flatten list
        tags_flat_list_cleaned = [i.replace(",", "") for i in tags_flat_list] # remove commas
        flat_list_sorted = sorted(set(list(filter(None, tags_flat_list_cleaned))), key=str.casefold) # remove emtpy, duplicates and sort
        return flat_list_sorted

    def add_tag(self, selected_tag, ui_tags_field):
        ui_tags_field.clearEditText()
        if selected_tag not in self.tmp_tags:
            self.tmp_tags += " " + str(selected_tag)
        ui_tags_field.setEditText(self.tmp_tags)

    def save_tmp_tags_from_field(self, selected_tag, ui_tags_field): # dirty way to save field before adding new tag (using item highlighted signal)
        self.tmp_tags = ui_tags_field.currentText()






# --------------------------------------------- OTHER ---------------------------------------------
    def add_to_search_history(self, which_history):
        # set history to be processed (shows or venues)
        if which_history == "shows":
            search_combobox = self.ui.cb_search_shows
            search_history_list = self.search_shows_history
        else:
            search_combobox = self.ui.cb_search_venues
            search_history_list = self.search_venues_history

        searched_text = search_combobox.currentText() # get search text
        search_history_list.insert(0, searched_text) # add new item at the beginning

        search_history_list = [x.strip() for x in search_history_list] # remove spaces
        search_history_list = list(filter(None, search_history_list)) # remove empty items
        search_history_list = list(dict.fromkeys(search_history_list)) # remove duplicates and keep order

        if len(search_history_list) > 20: # remove last item if list bigger than 20
            search_history_list.pop()

        search_history_list.insert(0, "") # add empty item at the beginning
        #print(search_history_list)
        current_search = search_combobox.currentText() # needed because of clear()
        search_combobox.clear()
        search_combobox.addItems(search_history_list)
        search_combobox.setEditText(current_search) # needed because of clear()

        # copy list back for saving
        if which_history == "shows":
            self.search_shows_history = search_history_list
        else:
            self.search_venues_history = search_history_list



    def on_venue_search_show(self):
        # search selected venue, click again to search previous search keyword
        venue_name = self.ui.field_venue_name.text()
        if self.ui.cb_search_shows.currentText() != venue_name:
            self.search_text = self.ui.cb_search_shows.currentText()
            self.ui.cb_search_shows.setCurrentText(venue_name)
        else:
            self.ui.cb_search_shows.setCurrentText(self.search_text)



    def on_venue_locate(self):
        address = self.ui.field_venue_address.toPlainText().replace(" ", "+").replace("\n", "+")
        if self.config_map_provider == "gmaps":
            url = "http://maps.google.com/?q=" + address
        else:
            url = "https://www.openstreetmap.org/search?query=" + address
        webbrowser.open(url)



    def on_venue_route(self):
        address = self.ui.field_venue_address.toPlainText().replace(" ", "+").replace("\n", "+")
        if self.config_map_provider == "gmaps":
            url = "http://maps.google.com/maps?saddr=" + self.config_homebase_city + "&daddr=" + address
        else:
            url = "https://www.openstreetmap.org/directions?from=" + self.config_homebase_city + "&to=" + address
        webbrowser.open(url)



    def on_venue_locate_geo_coordinates(self):
        geo = self.ui.field_venue_geocoordinates.text().replace(" ", "").split(",")
        if self.config_map_provider == "gmaps":
            url = "https://www.google.com/maps/place/" + geo[0] + "," + geo[1]
        else:
            url = "https://www.openstreetmap.org/?mlat=" + geo[0] + "&mlon=" + geo[1] + "&zoom=19"
        webbrowser.open(url)



    def on_show_website(self):
        webbrowser.open(self.ui.field_venue_website.text())


    def open_map(self):
        map.generate_map_with_venues(self.df_venues_in_list, self.config_homebase_city, self.config_homebase_geocoordinates)
        webbrowser.open("map.html")


    def open_calculator(self):
        self.calc_dialog = calc.CalcDialog(self)
        self.calc_dialog.show()

        self.ui.bt_calculator.setEnabled(False)
        self.ui.actionTravel_Costs_Calculator.setEnabled(False)




    def copy_monitor_text(self, what):
        self.clipboard = QGuiApplication.clipboard()
        if what == "selection":
            sel = self.ui.txt_monitor.textCursor().selectedText()
            if sel != "":
                self.clipboard.setText(sel)
                notify = "Text selection copied to clipboard!"
            else:
                notify = ""
                QMessageBox.information(self, "Copy Selection Error", "Please select some text in the monitor first.")
        else:
            self.clipboard.setText(self.ui.txt_monitor.toPlainText())
            notify = "Monitor content copied to clipboard!"
        self.ui.statusbar.showMessage(notify, 3000)



    def search_selected_text(self, where):
        sel = self.ui.txt_monitor.textCursor().selectedText().strip()
        if sel == "":
            #notify = "Please select some text first."
            #self.ui.statusbar.showMessage(notify, 3000)
            QMessageBox.information(self, "Search Selection Error","Please select some text in the monitor first.")
        else:
            if where == "shows":
                self.ui.cb_search_shows.setCurrentText(sel)
            elif where == "venues":
                self.ui.cb_search_venues.setCurrentText(sel)
            else:
                self.ui.cb_search_shows.setCurrentText(sel)
                self.ui.cb_search_venues.setCurrentText(sel)






    def open_custom_link(self, link):
        if "http" in link:
            webbrowser.open(link)
        else:
            gui_actions.open_file_or_folder(link)





    def on_about(self):
        text = ("A tool to easily organize shows and events.<br><br>"
                "Version: " + VERSION + "<br>"
                "Date: " + DATE + "<br>"
                "Developed by Vincent Rateau<br>"
                "License: GPL v.3<br><br>"
                "<a href='https://github.com/sonejostudios/TourManager'>https://github.com/sonejostudios/TourManager</a><br>")

        about = QMessageBox.about(self, "About", text)
        #about.setIconPixmap(QPixmap("logo.png"))




    def remove_lock_file(self):
        lock_file = os.path.join(self.config_workdir, LOCK_FILE)
        if os.path.exists(lock_file):
            print("LOCKED file deleted")
            os.remove(lock_file)




    def closeEvent(self, event):
        # trigger monitor combo box to save monitor notes
        self.ui.cb_monitor.setCurrentIndex(1)
        monitor.fill_monitor(self)

        # remove lock file
        self.remove_lock_file()

        # save needed stuff
        self.save_on_app_quit()


        # ask for saving before closing
        # close = QMessageBox.question(self, "QUIT", "Do you want to save the databases?", QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel, QMessageBox.Save)
        # if close == QMessageBox.Save:
        #     print("save database!")
        #     event.accept()
        # elif close == QMessageBox.Close:
        #     print("close app without saving database")
        #     event.accept()
        # else:
        #     print("go back to app")
        #     event.ignore()


        # bye bye
        print("Bye bye.")




    def save_on_app_quit(self):
        # auto export futureshows to html file if configured
        if self.config_auto_export_shows == "1":
            print("Future shows exported")
            exports.export_shows_to_html(self.df_shows, self.df_venues, self.config_workdir, self.ui)

        # auto export calendars if configured
        if self.config_auto_export_calendars == "1":
            print("Calendars exported")
            exports.export_all_calendars(self.df_shows, self.df_venues, self.config_workdir, self.ui, SHOW_STATUS)

        # save selected show if wanted on app start
        if self.config_start_with_selected_show == "1" and self.ui.list_show.currentItem() != None:
            selected_show = self.ui.list_show.currentItem().text()
            print("Save selected show:", selected_show)
            self.config.set("settings", "selected_show", selected_show)

        # write window size into config
        if self.config_save_window_size == "1":
            print("Window size saved")

            if self.isMaximized():
                self.config.set("gui", "start_maximized", "1")
            else:
                self.config.set("gui", "window_width", str(self.geometry().width()))
                self.config.set("gui", "window_height", str(self.geometry().height()))
                self.config.set("gui", "start_maximized", "0")

        # write histories
        self.config.set("histories", "search_shows_history", str(self.search_shows_history))
        self.config.set("histories", "search_venues_history", str(self.search_venues_history))


        # write config file
        with open(CONFIG_FILE, "w", encoding='utf-8') as configfile:
            self.config.write(configfile)







    def set_config_needs_restart(self, flag):
        self.config_needs_restart = flag


    def open_settings(self, show_tab):
        self.settings_dialog = settings.SettingsDialog(CONFIG_FILE, self, show_tab)
        ok = self.settings_dialog.exec() # modal (blocks main window)
        #ok = self.settings_dialog.show() # non modal

        # save gui geometry and other stuff (needed because of self.load_config())
        self.save_on_app_quit()

        if ok == 1: # accepted
            # force app restart if needed, otherwise reload config
            if self.config_needs_restart == True:
                QMessageBox.information(self, "Restart needed", "Please restart TourManager.")

                # try to save and close app
                try:
                    self.on_save_show()
                    self.on_save_venue()
                except:
                    pass

                self.remove_lock_file()
                sys.exit()

            else:
                # reload gui here to update all widgets
                self.load_config()






# --------------------------------------------- DEV ONLY ---------------------------------------------

    # only used in dev mode
    def show_show_in_table(self, show):
        # show in table
        selected_show = show.fillna("").astype(str)
        show_data = list(zip(selected_show.index, selected_show))
        table = self.ui.table_show
        table.setRowCount(len(show_data))
        table.setColumnCount(2)
        for i, (name, code) in enumerate(show_data):
            item_name = QTableWidgetItem(name)
            item_code = QTableWidgetItem(code)
            table.setItem(i, 0, item_name)
            table.setItem(i, 1, item_code)
        table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)



    def test(self):
        print("test!")

    def test_arg(self, arg):
        print(arg)








if __name__ == "__main__":
    app = QApplication(sys.argv)

    style = QStyleFactory.create('Fusion')
    app.setStyle(style)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


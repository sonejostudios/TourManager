from PySide6.QtWidgets import QTableWidgetItem, QDialog, QFileDialog, QAbstractItemView
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
import os

# import settings_dialog.py as module and it's main class
from settings_dialog import Ui_SettingsDialog



WORKDIR_TOOLTIP = ("The working folder with the databases, show folders, calendars, and all other relevant files.\n"
                   "If none, the application's folder (.) will be used.\n"
                   "For multi-user usage, select a the path to a mirrored cloud folder.\n\n"
                   "WARNING:\nIf no databases can't be found in the working folder, TourManager won't start!") # need a way to start settings even if no database found

GUI_THEMES = ["Fusion (Auto) (Default)", "PyQtDarkTheme (Auto)", "PyQtDarkTheme (Dark)", "PyQtDarkTheme (Light)"]

CALC_TEXT_DEC_SEP = ["comma (,)", "dot (.)"]
MAP_PROVIDER = ["osm", "gmaps"]

class SettingsDialog(QDialog):
    def __init__(self, CONFIG_FILE, parent, show_tab):
        super(SettingsDialog, self).__init__(parent)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Settings")

        # set vars
        self.p = parent
        self.CONFIG_FILE = CONFIG_FILE


        #populate fields and setup everything
        self.populate_fields()
        self.set_paths()
        self.populate_table_custom_links()


        # get theme index for later comparison
        self.current_theme_index = self.ui.field_theme.currentIndex()


        # setup for implementation of drag and drop in qtable from qt6.9
        self.ui.table_custom_links.setDragEnabled(True)
        self.ui.table_custom_links.setAcceptDrops(True)
        self.ui.table_custom_links.viewport().setAcceptDrops(True)
        self.ui.table_custom_links.setDragDropOverwriteMode(False)
        self.ui.table_custom_links.setDropIndicatorShown(True)
        self.ui.table_custom_links.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.ui.table_custom_links.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.table_custom_links.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)


        # show wanted tab
        if show_tab != None:
            self.ui.tabWidget.setCurrentIndex(show_tab)

        # hide unwanted widgets
        self.ui.bt_test.hide()



        # signals
        self.ui.field_workdir.textChanged.connect(self.set_paths)
        self.ui.bt_select_workdir.clicked.connect(self.select_workdir)

        self.ui.bt_copy_show_calendar.clicked.connect(lambda: self.copy_path(self.ui.field_show_calendar_path.text()))
        self.ui.bt_copy_event_calendar.clicked.connect(lambda: self.copy_path(self.ui.field_event_calendar_path.text()))
        self.ui.bt_copy_event_forecast_calendar.clicked.connect(lambda: self.copy_path(self.ui.field_event_forecast_calendar_path.text()))

        self.ui.bt_insert_link.clicked.connect(lambda: self.insert_link(""))
        self.ui.bt_insert_separator.clicked.connect(lambda: self.insert_link("|"))
        self.ui.bt_delete_link.clicked.connect(self.delete_link)
        self.ui.bt_test.clicked.connect(self.get_custom_links_list)




# --------------------------Accept and Save--------------------------

    def accept(self):
        if self.p.config_workdir != self.ui.field_workdir.text():
            # self.p.remove_lock_file()
            self.p.set_config_needs_restart(True)

        if self.ui.field_theme.currentIndex() != self.current_theme_index:
            self.p.set_config_needs_restart(True)

        self.save_settings()
        super().accept()

    def save_settings(self):
        # save variables and config (config is reloaded after accept())
        self.p.config.set("defaults", "homebase_city", self.ui.field_homebase_city.text())
        self.p.config.set("defaults", "homebase_geocoordinates", self.ui.field_geocoordinates.text())
        self.p.config.set("defaults", "artist", self.ui.field_artist.text())
        self.p.config.set("defaults", "currency", self.ui.field_currency.text())
        self.p.config.set("defaults", "distance_unit", self.ui.field_distance_unit.text())
        self.p.config.set("defaults", "travel_unit_price", str(self.ui.field_travel_unit_price.value()))

        # theme
        if self.ui.field_theme.currentIndex() == 1:
            self.p.config.set("gui", "theme", "auto")
        elif self.ui.field_theme.currentIndex() == 2:
            self.p.config.set("gui", "theme", "dark")
        elif self.ui.field_theme.currentIndex() == 3:
            self.p.config.set("gui", "theme", "light")
        else:
            self.p.config.set("gui", "theme", "")

        self.p.config.set("gui", "font_size", str(self.ui.field_fontsize.value()))
        self.p.config.set("gui", "field_area_width", str(self.ui.field_field_area_width.value()))

        self.p.config.set("gui", "save_window_size", str(int(self.ui.field_save_window_size.isChecked())))
        self.p.config.set("settings", "start_with_selected_show",
                          str(int(self.ui.field_start_with_selected_show.isChecked())))

        if self.ui.field_calc_text_decimal_separator.currentIndex() == 0:
            self.p.config.set("settings", "calc_text_decimal_separator", ",")
        else:
            self.p.config.set("settings", "calc_text_decimal_separator", ".")

        self.p.config.set("settings", "map_provider", self.ui.field_map_provider.currentText())

        # paths and exports
        self.p.config.set("paths", "working_directory", self.ui.field_workdir.text())

        self.p.config.set("settings", "auto_export_shows", str(int(self.ui.field_auto_export_shows.isChecked())))
        self.p.config.set("settings", "auto_export_calendars",
                          str(int(self.ui.field_auto_export_calendars.isChecked())))

        # custom links
        self.p.config.set("settings", "custom_links", str(self.get_custom_links_list()))




        # write config file
        with open(self.CONFIG_FILE, "w", encoding='utf-8') as configfile:
            self.p.config.write(configfile)






    # --------------------------Defaults and Interface--------------------------

    def populate_fields(self):
        # defaults
        self.ui.field_homebase_city.setText(self.p.config_homebase_city)
        self.ui.field_geocoordinates.setText(self.p.config_homebase_geocoordinates)
        self.ui.field_artist.setText(self.p.config_artist)
        self.ui.field_currency.setText(self.p.config_currency)
        self.ui.field_distance_unit.setText(self.p.config_distance_unit)
        self.ui.field_travel_unit_price.setValue(self.p.config_travel_unit_price)

        # view
        self.ui.field_theme.addItems(GUI_THEMES)
        if self.p.config_theme == "auto":
            self.ui.field_theme.setCurrentIndex(1)
        elif self.p.config_theme == "dark":
            self.ui.field_theme.setCurrentIndex(2)
        elif self.p.config_theme == "light":
            self.ui.field_theme.setCurrentIndex(3)
        else:
            self.ui.field_theme.setCurrentIndex(0)


        self.ui.field_fontsize.setValue(int(self.p.config_font_size))
        self.ui.field_field_area_width.setValue(int(self.p.config_field_area_width))

        self.ui.field_save_window_size.setChecked(int(self.p.config_save_window_size))
        self.ui.field_start_with_selected_show.setChecked(int(self.p.config_start_with_selected_show))

        self.ui.field_calc_text_decimal_separator.addItems(CALC_TEXT_DEC_SEP)
        if self.p.config_calc_dec_sep == ",":
            self.ui.field_calc_text_decimal_separator.setCurrentIndex(0)
        else:
            self.ui.field_calc_text_decimal_separator.setCurrentIndex(1)

        self.ui.field_map_provider.addItems(MAP_PROVIDER)
        self.ui.field_map_provider.setCurrentText(self.p.config_map_provider)
        

        # paths and exports
        self.ui.field_workdir.setText(self.p.config_workdir)
        self.ui.field_workdir.setToolTip(WORKDIR_TOOLTIP)
        self.ui.field_auto_export_shows.setChecked(int(self.p.config_auto_export_shows))
        self.ui.field_auto_export_calendars.setChecked(int(self.p.config_auto_export_calendars))



# --------------------------Paths and Exports-------------------------

    def select_workdir(self):
        dir = QFileDialog.getExistingDirectory(self, "Select a Working Folder", "", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.ui.field_workdir.setText(dir)

    def set_paths(self):
        workdir = self.ui.field_workdir.text()
        workdir_abs = os.path.abspath(workdir)
        calendar_shows = os.path.abspath(os.path.join(workdir, "TourManagerShows.ics"))
        self.ui.field_show_calendar_path.setText(calendar_shows)
        calendar_events = os.path.abspath(os.path.join(workdir, "TourManagerEvents.ics"))
        self.ui.field_event_calendar_path.setText(calendar_events)
        calendar_events_forecast = os.path.abspath(os.path.join(workdir, "TourManagerEventsForecast.ics"))
        self.ui.field_event_forecast_calendar_path.setText(calendar_events_forecast)

    def copy_path(self, path):
        self.clipboard = QGuiApplication.clipboard()
        self.clipboard.setText(path)
        print(path, "copied!")
        self.p.ui.statusbar.showMessage("Path copied to clipboard!", 3000)





#--------------------------Custom links--------------------------

    def populate_table_custom_links(self):
        links_list = eval(self.p.config_custom_links)
        print(links_list)

        table = self.ui.table_custom_links
        table.setRowCount(len(links_list))
        table.setColumnCount(2)

        for i, (name, link) in enumerate(links_list):
            item_name = QTableWidgetItem(name)
            item_name.setFlags(~Qt.ItemIsDropEnabled) # set item flags to drop = disabled
            item_link = QTableWidgetItem(link)
            item_link.setFlags(~Qt.ItemIsDropEnabled) # set item flags to drop = disabled
            table.setItem(i, 0, item_name)
            table.setItem(i, 1, item_link)


    def insert_link(self, name):
        table = self.ui.table_custom_links
        selected_cells = table.selectedIndexes()
        if len(selected_cells) > 0:
            selected_row_index = selected_cells[0].row()
            table.insertRow(selected_row_index + 1) # insert link after selected. or better insert before?
            if name != "": # add "name" to first cell and "" to second
                item_name = QTableWidgetItem(name)
                item_link = QTableWidgetItem("")
                table.setItem(selected_row_index + 1, 0, item_name)
                table.setItem(selected_row_index + 1, 1, item_link)


    def delete_link(self):
        table = self.ui.table_custom_links
        selected_cells = table.selectedIndexes()
        print(selected_cells)
        if len(selected_cells) > 0:
            selected_row_index = selected_cells[0].row()
            table.removeRow(selected_row_index)



    def get_custom_links_list(self):
        custom_links = []
        table = self.ui.table_custom_links
        for row in range(table.rowCount()):
            item_0 = table.item(row, 0)
            item_1 = table.item(row, 1)
            if item_0 and item_1:
                custom_links.append((item_0.text(), item_1.text()))
        return custom_links

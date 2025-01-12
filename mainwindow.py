# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFormLayout, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1660, 1006)
        self.actionBackup = QAction(MainWindow)
        self.actionBackup.setObjectName(u"actionBackup")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionUpcoming_Shows = QAction(MainWindow)
        self.actionUpcoming_Shows.setObjectName(u"actionUpcoming_Shows")
        self.actionCalendars = QAction(MainWindow)
        self.actionCalendars.setObjectName(u"actionCalendars")
        self.actionOpen_Working_Folder = QAction(MainWindow)
        self.actionOpen_Working_Folder.setObjectName(u"actionOpen_Working_Folder")
        self.actionOpen_Show_Folder = QAction(MainWindow)
        self.actionOpen_Show_Folder.setObjectName(u"actionOpen_Show_Folder")
        self.actionOpen_Backup_Folder = QAction(MainWindow)
        self.actionOpen_Backup_Folder.setObjectName(u"actionOpen_Backup_Folder")
        self.actionOpen_Root_Folder = QAction(MainWindow)
        self.actionOpen_Root_Folder.setObjectName(u"actionOpen_Root_Folder")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionTravel_Costs_Calculator = QAction(MainWindow)
        self.actionTravel_Costs_Calculator.setObjectName(u"actionTravel_Costs_Calculator")
        self.actionMap = QAction(MainWindow)
        self.actionMap.setObjectName(u"actionMap")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_16 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_34)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.field_show_dateedit = QDateEdit(self.centralwidget)
        self.field_show_dateedit.setObjectName(u"field_show_dateedit")
        self.field_show_dateedit.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.field_show_dateedit)

        self.field_show_id = QLineEdit(self.centralwidget)
        self.field_show_id.setObjectName(u"field_show_id")
        self.field_show_id.setMaximumSize(QSize(36, 16777215))
        self.field_show_id.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.field_show_id)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_29)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.field_venue_text = QLineEdit(self.centralwidget)
        self.field_venue_text.setObjectName(u"field_venue_text")
        self.field_venue_text.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.field_venue_text)

        self.field_venue_id = QLineEdit(self.centralwidget)
        self.field_venue_id.setObjectName(u"field_venue_id")
        self.field_venue_id.setMaximumSize(QSize(36, 16777215))
        self.field_venue_id.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.field_venue_id)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.cb_show_status = QComboBox(self.centralwidget)
        self.cb_show_status.setObjectName(u"cb_show_status")
        self.cb_show_status.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_show_status)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label)

        self.field_show_artists = QLineEdit(self.centralwidget)
        self.field_show_artists.setObjectName(u"field_show_artists")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.field_show_artists)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_15)

        self.field_show_contact = QLineEdit(self.centralwidget)
        self.field_show_contact.setObjectName(u"field_show_contact")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.field_show_contact)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_16)

        self.field_show_phone = QLineEdit(self.centralwidget)
        self.field_show_phone.setObjectName(u"field_show_phone")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.field_show_phone)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_17)

        self.field_show_email = QLineEdit(self.centralwidget)
        self.field_show_email.setObjectName(u"field_show_email")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.field_show_email)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_18)

        self.field_show_tech_contact = QLineEdit(self.centralwidget)
        self.field_show_tech_contact.setObjectName(u"field_show_tech_contact")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.field_show_tech_contact)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_19)

        self.field_show_tech_phone = QLineEdit(self.centralwidget)
        self.field_show_tech_phone.setObjectName(u"field_show_tech_phone")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.field_show_tech_phone)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_20)

        self.field_show_tech_email = QLineEdit(self.centralwidget)
        self.field_show_tech_email.setObjectName(u"field_show_tech_email")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.field_show_tech_email)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_25)

        self.bt_show_folder = QPushButton(self.centralwidget)
        self.bt_show_folder.setObjectName(u"bt_show_folder")
        self.bt_show_folder.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.bt_show_folder)

        self.arrivalTimeLabel = QLabel(self.centralwidget)
        self.arrivalTimeLabel.setObjectName(u"arrivalTimeLabel")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.arrivalTimeLabel)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.field_show_arrival_time = QLineEdit(self.centralwidget)
        self.field_show_arrival_time.setObjectName(u"field_show_arrival_time")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_show_arrival_time.sizePolicy().hasHeightForWidth())
        self.field_show_arrival_time.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.field_show_arrival_time, 1, 1, 1, 1)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_30, 0, 1, 1, 1)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_22, 0, 2, 1, 1)

        self.field_show_soundcheck_time = QLineEdit(self.centralwidget)
        self.field_show_soundcheck_time.setObjectName(u"field_show_soundcheck_time")
        sizePolicy.setHeightForWidth(self.field_show_soundcheck_time.sizePolicy().hasHeightForWidth())
        self.field_show_soundcheck_time.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.field_show_soundcheck_time, 1, 2, 1, 1)

        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_31, 2, 1, 1, 1)

        self.field_show_opening_time = QLineEdit(self.centralwidget)
        self.field_show_opening_time.setObjectName(u"field_show_opening_time")
        sizePolicy.setHeightForWidth(self.field_show_opening_time.sizePolicy().hasHeightForWidth())
        self.field_show_opening_time.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.field_show_opening_time, 3, 1, 1, 1)

        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_26, 2, 2, 1, 1)

        self.field_show_show_time = QLineEdit(self.centralwidget)
        self.field_show_show_time.setObjectName(u"field_show_show_time")
        sizePolicy.setHeightForWidth(self.field_show_show_time.sizePolicy().hasHeightForWidth())
        self.field_show_show_time.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.field_show_show_time, 3, 2, 1, 1)


        self.formLayout.setLayout(11, QFormLayout.FieldRole, self.gridLayout)

        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_23)

        self.field_show_info = QPlainTextEdit(self.centralwidget)
        self.field_show_info.setObjectName(u"field_show_info")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.field_show_info.sizePolicy().hasHeightForWidth())
        self.field_show_info.setSizePolicy(sizePolicy2)
        self.field_show_info.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.field_show_info)

        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_21)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.field_show_fee = QLineEdit(self.centralwidget)
        self.field_show_fee.setObjectName(u"field_show_fee")

        self.horizontalLayout_5.addWidget(self.field_show_fee)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.field_show_travel_fee = QLineEdit(self.centralwidget)
        self.field_show_travel_fee.setObjectName(u"field_show_travel_fee")

        self.horizontalLayout_5.addWidget(self.field_show_travel_fee)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.field_show_fee_sum = QLineEdit(self.centralwidget)
        self.field_show_fee_sum.setObjectName(u"field_show_fee_sum")
        self.field_show_fee_sum.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.field_show_fee_sum)

        self.field_show_currency = QLineEdit(self.centralwidget)
        self.field_show_currency.setObjectName(u"field_show_currency")
        self.field_show_currency.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_5.addWidget(self.field_show_currency)


        self.formLayout.setLayout(13, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.accomodationLabel_2 = QLabel(self.centralwidget)
        self.accomodationLabel_2.setObjectName(u"accomodationLabel_2")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.accomodationLabel_2)

        self.field_show_food_drinks = QLineEdit(self.centralwidget)
        self.field_show_food_drinks.setObjectName(u"field_show_food_drinks")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.field_show_food_drinks)

        self.accomodationLabel = QLabel(self.centralwidget)
        self.accomodationLabel.setObjectName(u"accomodationLabel")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.accomodationLabel)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.field_show_accomodation = QLineEdit(self.centralwidget)
        self.field_show_accomodation.setObjectName(u"field_show_accomodation")

        self.horizontalLayout_8.addWidget(self.field_show_accomodation)

        self.field_show_breakfast = QLineEdit(self.centralwidget)
        self.field_show_breakfast.setObjectName(u"field_show_breakfast")

        self.horizontalLayout_8.addWidget(self.field_show_breakfast)


        self.formLayout.setLayout(15, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.printLabel = QLabel(self.centralwidget)
        self.printLabel.setObjectName(u"printLabel")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.printLabel)

        self.field_show_print = QLineEdit(self.centralwidget)
        self.field_show_print.setObjectName(u"field_show_print")

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.field_show_print)

        self.addressForPrintLabel = QLabel(self.centralwidget)
        self.addressForPrintLabel.setObjectName(u"addressForPrintLabel")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.addressForPrintLabel)

        self.field_show_print_address = QPlainTextEdit(self.centralwidget)
        self.field_show_print_address.setObjectName(u"field_show_print_address")
        self.field_show_print_address.setMaximumSize(QSize(16777215, 60))

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.field_show_print_address)

        self.tagsLabel = QLabel(self.centralwidget)
        self.tagsLabel.setObjectName(u"tagsLabel")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.tagsLabel)

        self.field_show_tags = QLineEdit(self.centralwidget)
        self.field_show_tags.setObjectName(u"field_show_tags")
        self.field_show_tags.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.field_show_tags)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.bt_save_show = QPushButton(self.centralwidget)
        self.bt_save_show.setObjectName(u"bt_save_show")
        self.bt_save_show.setMinimumSize(QSize(0, 41))

        self.horizontalLayout_10.addWidget(self.bt_save_show)

        self.bt_new_show = QPushButton(self.centralwidget)
        self.bt_new_show.setObjectName(u"bt_new_show")
        self.bt_new_show.setMinimumSize(QSize(0, 41))

        self.horizontalLayout_10.addWidget(self.bt_new_show)

        self.bt_duplicate_show = QPushButton(self.centralwidget)
        self.bt_duplicate_show.setObjectName(u"bt_duplicate_show")
        self.bt_duplicate_show.setMinimumSize(QSize(0, 41))

        self.horizontalLayout_10.addWidget(self.bt_duplicate_show)

        self.bt_delete_show = QPushButton(self.centralwidget)
        self.bt_delete_show.setObjectName(u"bt_delete_show")
        self.bt_delete_show.setMinimumSize(QSize(0, 41))

        self.horizontalLayout_10.addWidget(self.bt_delete_show)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalLayout_2.setStretch(1, 10)

        self.horizontalLayout_16.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_search_shows = QLineEdit(self.centralwidget)
        self.lineEdit_search_shows.setObjectName(u"lineEdit_search_shows")
        self.lineEdit_search_shows.setMinimumSize(QSize(160, 31))
        self.lineEdit_search_shows.setClearButtonEnabled(True)

        self.horizontalLayout_12.addWidget(self.lineEdit_search_shows)

        self.cb_show_status_filter = QComboBox(self.centralwidget)
        self.cb_show_status_filter.setObjectName(u"cb_show_status_filter")
        self.cb_show_status_filter.setMinimumSize(QSize(160, 31))

        self.horizontalLayout_12.addWidget(self.cb_show_status_filter)

        self.label_show_amount = QLabel(self.centralwidget)
        self.label_show_amount.setObjectName(u"label_show_amount")
        self.label_show_amount.setMinimumSize(QSize(31, 0))
        self.label_show_amount.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_12.addWidget(self.label_show_amount)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.list_show = QListWidget(self.centralwidget)
        self.list_show.setObjectName(u"list_show")

        self.verticalLayout_3.addWidget(self.list_show)

        self.cb_monitor = QComboBox(self.centralwidget)
        self.cb_monitor.setObjectName(u"cb_monitor")
        self.cb_monitor.setMinimumSize(QSize(0, 31))

        self.verticalLayout_3.addWidget(self.cb_monitor)


        self.horizontalLayout_15.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_search_venues = QLineEdit(self.centralwidget)
        self.lineEdit_search_venues.setObjectName(u"lineEdit_search_venues")
        self.lineEdit_search_venues.setMinimumSize(QSize(160, 31))
        self.lineEdit_search_venues.setClearButtonEnabled(True)

        self.horizontalLayout_13.addWidget(self.lineEdit_search_venues)

        self.cb_venue_filter = QComboBox(self.centralwidget)
        self.cb_venue_filter.setObjectName(u"cb_venue_filter")
        self.cb_venue_filter.setMinimumSize(QSize(160, 31))

        self.horizontalLayout_13.addWidget(self.cb_venue_filter)

        self.label_venue_amount = QLabel(self.centralwidget)
        self.label_venue_amount.setObjectName(u"label_venue_amount")
        self.label_venue_amount.setMinimumSize(QSize(31, 0))
        self.label_venue_amount.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_13.addWidget(self.label_venue_amount)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.list_venue = QListWidget(self.centralwidget)
        self.list_venue.setObjectName(u"list_venue")

        self.verticalLayout_4.addWidget(self.list_venue)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.bt_map = QPushButton(self.centralwidget)
        self.bt_map.setObjectName(u"bt_map")
        self.bt_map.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_14.addWidget(self.bt_map)

        self.bt_calculator = QPushButton(self.centralwidget)
        self.bt_calculator.setObjectName(u"bt_calculator")
        self.bt_calculator.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_14.addWidget(self.bt_calculator)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_15.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.txt_monitor = QPlainTextEdit(self.centralwidget)
        self.txt_monitor.setObjectName(u"txt_monitor")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(10)
        self.txt_monitor.setFont(font)

        self.verticalLayout_5.addWidget(self.txt_monitor)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.table_show = QTableWidget(self.centralwidget)
        if (self.table_show.columnCount() < 2):
            self.table_show.setColumnCount(2)
        self.table_show.setObjectName(u"table_show")
        self.table_show.setColumnCount(2)
        self.table_show.horizontalHeader().setVisible(False)
        self.table_show.horizontalHeader().setCascadingSectionResizes(True)
        self.table_show.horizontalHeader().setDefaultSectionSize(150)
        self.table_show.horizontalHeader().setStretchLastSection(True)
        self.table_show.verticalHeader().setVisible(False)

        self.horizontalLayout_11.addWidget(self.table_show)

        self.my_button = QPushButton(self.centralwidget)
        self.my_button.setObjectName(u"my_button")

        self.horizontalLayout_11.addWidget(self.my_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalLayout_5.setStretch(1, 10)
        self.verticalLayout_5.setStretch(2, 5)

        self.horizontalLayout_16.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_36)

        self.lb_homebase = QLabel(self.centralwidget)
        self.lb_homebase.setObjectName(u"lb_homebase")
        self.lb_homebase.setMinimumSize(QSize(0, 31))
        self.lb_homebase.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lb_homebase)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.field_venue_name = QLineEdit(self.centralwidget)
        self.field_venue_name.setObjectName(u"field_venue_name")

        self.horizontalLayout_7.addWidget(self.field_venue_name)

        self.bt_venue_search_shows = QPushButton(self.centralwidget)
        self.bt_venue_search_shows.setObjectName(u"bt_venue_search_shows")
        self.bt_venue_search_shows.setMinimumSize(QSize(0, 12))
        self.bt_venue_search_shows.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_7.addWidget(self.bt_venue_search_shows)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.field_venue_city = QLineEdit(self.centralwidget)
        self.field_venue_city.setObjectName(u"field_venue_city")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.field_venue_city)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.field_venue_country = QLineEdit(self.centralwidget)
        self.field_venue_country.setObjectName(u"field_venue_country")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.field_venue_country)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.field_venue_address = QPlainTextEdit(self.centralwidget)
        self.field_venue_address.setObjectName(u"field_venue_address")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.field_venue_address.sizePolicy().hasHeightForWidth())
        self.field_venue_address.setSizePolicy(sizePolicy3)
        self.field_venue_address.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout.addWidget(self.field_venue_address)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bt_venue_locate = QPushButton(self.centralwidget)
        self.bt_venue_locate.setObjectName(u"bt_venue_locate")
        self.bt_venue_locate.setMinimumSize(QSize(0, 0))
        self.bt_venue_locate.setMaximumSize(QSize(60, 30))

        self.verticalLayout.addWidget(self.bt_venue_locate)

        self.bt_venue_route = QPushButton(self.centralwidget)
        self.bt_venue_route.setObjectName(u"bt_venue_route")
        self.bt_venue_route.setMinimumSize(QSize(60, 0))
        self.bt_venue_route.setMaximumSize(QSize(60, 30))

        self.verticalLayout.addWidget(self.bt_venue_route)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_32)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_28)

        self.field_checkbox_venue_is_event = QCheckBox(self.centralwidget)
        self.field_checkbox_venue_is_event.setObjectName(u"field_checkbox_venue_is_event")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.field_checkbox_venue_is_event)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_14)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.field_venue_start_dateedit = QDateEdit(self.centralwidget)
        self.field_venue_start_dateedit.setObjectName(u"field_venue_start_dateedit")
        self.field_venue_start_dateedit.setMinimumDate(QDate(1752, 9, 14))
        self.field_venue_start_dateedit.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.field_venue_start_dateedit)

        self.field_venue_end_dateedit = QDateEdit(self.centralwidget)
        self.field_venue_end_dateedit.setObjectName(u"field_venue_end_dateedit")
        self.field_venue_end_dateedit.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.field_venue_end_dateedit)


        self.formLayout_2.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.field_venue_website = QLineEdit(self.centralwidget)
        self.field_venue_website.setObjectName(u"field_venue_website")

        self.horizontalLayout_2.addWidget(self.field_venue_website)

        self.bt_website = QPushButton(self.centralwidget)
        self.bt_website.setObjectName(u"bt_website")
        self.bt_website.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2.addWidget(self.bt_website)


        self.formLayout_2.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_33)

        self.field_venue_genres = QLineEdit(self.centralwidget)
        self.field_venue_genres.setObjectName(u"field_venue_genres")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.field_venue_genres)

        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_35)

        self.cb_venue_rating = QComboBox(self.centralwidget)
        self.cb_venue_rating.setObjectName(u"cb_venue_rating")
        self.cb_venue_rating.setMinimumSize(QSize(0, 0))
        self.cb_venue_rating.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.cb_venue_rating.setFont(font1)
        self.cb_venue_rating.setFrame(True)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.cb_venue_rating)

        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_27)

        self.field_checkbox_venue_is_discontinued = QCheckBox(self.centralwidget)
        self.field_checkbox_venue_is_discontinued.setObjectName(u"field_checkbox_venue_is_discontinued")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.field_checkbox_venue_is_discontinued)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.label_11)

        self.field_venue_contact = QLineEdit(self.centralwidget)
        self.field_venue_contact.setObjectName(u"field_venue_contact")

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.field_venue_contact)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_12)

        self.field_venue_phone = QLineEdit(self.centralwidget)
        self.field_venue_phone.setObjectName(u"field_venue_phone")

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.field_venue_phone)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.label_13)

        self.field_venue_email = QLineEdit(self.centralwidget)
        self.field_venue_email.setObjectName(u"field_venue_email")

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.field_venue_email)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.label_10)

        self.field_venue_info = QPlainTextEdit(self.centralwidget)
        self.field_venue_info.setObjectName(u"field_venue_info")

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.field_venue_info)

        self.tagsLabel_2 = QLabel(self.centralwidget)
        self.tagsLabel_2.setObjectName(u"tagsLabel_2")

        self.formLayout_2.setWidget(16, QFormLayout.LabelRole, self.tagsLabel_2)

        self.field_venue_tags = QLineEdit(self.centralwidget)
        self.field_venue_tags.setObjectName(u"field_venue_tags")
        self.field_venue_tags.setMinimumSize(QSize(0, 0))

        self.formLayout_2.setWidget(16, QFormLayout.FieldRole, self.field_venue_tags)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.field_venue_geocoordinates = QLineEdit(self.centralwidget)
        self.field_venue_geocoordinates.setObjectName(u"field_venue_geocoordinates")

        self.horizontalLayout_17.addWidget(self.field_venue_geocoordinates)

        self.bt_venue_locate_geocoordinates = QPushButton(self.centralwidget)
        self.bt_venue_locate_geocoordinates.setObjectName(u"bt_venue_locate_geocoordinates")
        self.bt_venue_locate_geocoordinates.setMinimumSize(QSize(0, 0))
        self.bt_venue_locate_geocoordinates.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_17.addWidget(self.bt_venue_locate_geocoordinates)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_17)


        self.verticalLayout_6.addLayout(self.formLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.bt_save_venue = QPushButton(self.centralwidget)
        self.bt_save_venue.setObjectName(u"bt_save_venue")
        self.bt_save_venue.setMinimumSize(QSize(0, 41))

        self.horizontalLayout_9.addWidget(self.bt_save_venue)

        self.bt_new_venue = QPushButton(self.centralwidget)
        self.bt_new_venue.setObjectName(u"bt_new_venue")
        self.bt_new_venue.setMinimumSize(QSize(0, 41))

        self.horizontalLayout_9.addWidget(self.bt_new_venue)

        self.bt_delete_venue = QPushButton(self.centralwidget)
        self.bt_delete_venue.setObjectName(u"bt_delete_venue")
        self.bt_delete_venue.setMinimumSize(QSize(0, 41))

        self.horizontalLayout_9.addWidget(self.bt_delete_venue)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_16.addLayout(self.verticalLayout_6)

        self.horizontalLayout_16.setStretch(0, 2)
        self.horizontalLayout_16.setStretch(1, 10)
        self.horizontalLayout_16.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1660, 20))
        self.menuDatabases = QMenu(self.menubar)
        self.menuDatabases.setObjectName(u"menuDatabases")
        self.menuExport = QMenu(self.menubar)
        self.menuExport.setObjectName(u"menuExport")
        self.menuFolders = QMenu(self.menubar)
        self.menuFolders.setObjectName(u"menuFolders")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatabases.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuFolders.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuDatabases.addAction(self.actionBackup)
        self.menuDatabases.addSeparator()
        self.menuDatabases.addAction(self.actionQuit)
        self.menuExport.addAction(self.actionUpcoming_Shows)
        self.menuExport.addSeparator()
        self.menuExport.addAction(self.actionCalendars)
        self.menuFolders.addAction(self.actionOpen_Working_Folder)
        self.menuFolders.addAction(self.actionOpen_Show_Folder)
        self.menuFolders.addAction(self.actionOpen_Backup_Folder)
        self.menuFolders.addAction(self.actionOpen_Root_Folder)
        self.menuInfo.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionMap)
        self.menuTools.addAction(self.actionTravel_Costs_Calculator)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionBackup.setText(QCoreApplication.translate("MainWindow", u"Backup Now", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionUpcoming_Shows.setText(QCoreApplication.translate("MainWindow", u"Upcoming Shows (.html)", None))
        self.actionCalendars.setText(QCoreApplication.translate("MainWindow", u"Calendars (.ics)", None))
        self.actionOpen_Working_Folder.setText(QCoreApplication.translate("MainWindow", u"Working Folder", None))
        self.actionOpen_Show_Folder.setText(QCoreApplication.translate("MainWindow", u"Shows", None))
        self.actionOpen_Backup_Folder.setText(QCoreApplication.translate("MainWindow", u"Backups", None))
        self.actionOpen_Root_Folder.setText(QCoreApplication.translate("MainWindow", u"Application Folder", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionTravel_Costs_Calculator.setText(QCoreApplication.translate("MainWindow", u"Travel Costs Calculator", None))
        self.actionMap.setText(QCoreApplication.translate("MainWindow", u"Map", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"SHOWS", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.field_show_dateedit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
#if QT_CONFIG(tooltip)
        self.field_show_id.setToolTip(QCoreApplication.translate("MainWindow", u"ShowID", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Venue", None))
#if QT_CONFIG(tooltip)
        self.field_venue_id.setToolTip(QCoreApplication.translate("MainWindow", u"VenueID", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.field_venue_id.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.field_venue_id.setPlaceholderText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Booking Status", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Artist(s)", None))
#if QT_CONFIG(tooltip)
        self.field_show_artists.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.field_show_artists.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
#if QT_CONFIG(tooltip)
        self.field_show_contact.setToolTip(QCoreApplication.translate("MainWindow", u"Contact person", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Technician", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Tech Phone", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tech Email", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Show Folder", None))
#if QT_CONFIG(tooltip)
        self.bt_show_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Create or open Show Folder", None))
#endif // QT_CONFIG(tooltip)
        self.bt_show_folder.setText(QCoreApplication.translate("MainWindow", u"Show Folder", None))
        self.arrivalTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Arrival", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Soundcheck", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Doors Opening", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Show Time", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Fee + Travel Costs", None))
#if QT_CONFIG(tooltip)
        self.field_show_fee.setToolTip(QCoreApplication.translate("MainWindow", u"Fee", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.field_show_travel_fee.setToolTip(QCoreApplication.translate("MainWindow", u"Travel Costs", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(tooltip)
        self.field_show_fee_sum.setToolTip(QCoreApplication.translate("MainWindow", u"SUM", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.field_show_currency.setToolTip(QCoreApplication.translate("MainWindow", u"Currency", None))
#endif // QT_CONFIG(tooltip)
        self.accomodationLabel_2.setText(QCoreApplication.translate("MainWindow", u"Food & Drinks", None))
        self.accomodationLabel.setText(QCoreApplication.translate("MainWindow", u"Bed & Breakfast", None))
#if QT_CONFIG(tooltip)
        self.field_show_accomodation.setToolTip(QCoreApplication.translate("MainWindow", u"Bed (Accomodation)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.field_show_breakfast.setToolTip(QCoreApplication.translate("MainWindow", u"Breakfast", None))
#endif // QT_CONFIG(tooltip)
        self.printLabel.setText(QCoreApplication.translate("MainWindow", u"Print", None))
#if QT_CONFIG(tooltip)
        self.field_show_print.setToolTip(QCoreApplication.translate("MainWindow", u"Print material to be send (posters, amount, ...)", None))
#endif // QT_CONFIG(tooltip)
        self.addressForPrintLabel.setText(QCoreApplication.translate("MainWindow", u"Address for Print", None))
#if QT_CONFIG(tooltip)
        self.field_show_print_address.setToolTip(QCoreApplication.translate("MainWindow", u"Address where to send print material", None))
#endif // QT_CONFIG(tooltip)
        self.tagsLabel.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
#if QT_CONFIG(tooltip)
        self.field_show_tags.setToolTip(QCoreApplication.translate("MainWindow", u"E.g. #release-tour, #black-list", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bt_save_show.setToolTip(QCoreApplication.translate("MainWindow", u"Save current Show", None))
#endif // QT_CONFIG(tooltip)
        self.bt_save_show.setText(QCoreApplication.translate("MainWindow", u"Save Show", None))
#if QT_CONFIG(tooltip)
        self.bt_new_show.setToolTip(QCoreApplication.translate("MainWindow", u"Add a new Show", None))
#endif // QT_CONFIG(tooltip)
        self.bt_new_show.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
#if QT_CONFIG(tooltip)
        self.bt_duplicate_show.setToolTip(QCoreApplication.translate("MainWindow", u"Duplicate current Show", None))
#endif // QT_CONFIG(tooltip)
        self.bt_duplicate_show.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
#if QT_CONFIG(tooltip)
        self.bt_delete_show.setToolTip(QCoreApplication.translate("MainWindow", u"Delete current Show", None))
#endif // QT_CONFIG(tooltip)
        self.bt_delete_show.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_search_shows.setToolTip(QCoreApplication.translate("MainWindow", u"Show Search", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_search_shows.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Shows...", None))
#if QT_CONFIG(tooltip)
        self.cb_show_status_filter.setToolTip(QCoreApplication.translate("MainWindow", u"Show Status Filter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_show_amount.setToolTip(QCoreApplication.translate("MainWindow", u"Amount of Shows in list", None))
#endif // QT_CONFIG(tooltip)
        self.label_show_amount.setText(QCoreApplication.translate("MainWindow", u"SHO", None))
#if QT_CONFIG(tooltip)
        self.cb_monitor.setToolTip(QCoreApplication.translate("MainWindow", u"Monitor Selection\n"
"Get Information according to Searches and Filters\n"
"(except Notes and Paths)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_search_venues.setToolTip(QCoreApplication.translate("MainWindow", u"Venue Search", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_search_venues.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Venues...", None))
#if QT_CONFIG(tooltip)
        self.cb_venue_filter.setToolTip(QCoreApplication.translate("MainWindow", u"Venue Filter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_venue_amount.setToolTip(QCoreApplication.translate("MainWindow", u"Amount of Venues in list", None))
#endif // QT_CONFIG(tooltip)
        self.label_venue_amount.setText(QCoreApplication.translate("MainWindow", u"VEN", None))
#if QT_CONFIG(tooltip)
        self.bt_map.setToolTip(QCoreApplication.translate("MainWindow", u"Open Venue Map according to Venue Filter and Venue Search", None))
#endif // QT_CONFIG(tooltip)
        self.bt_map.setText(QCoreApplication.translate("MainWindow", u"Map", None))
#if QT_CONFIG(tooltip)
        self.bt_calculator.setToolTip(QCoreApplication.translate("MainWindow", u"Open Travel Costs Calculator", None))
#endif // QT_CONFIG(tooltip)
        self.bt_calculator.setText(QCoreApplication.translate("MainWindow", u"Travel Costs Calculator", None))
#if QT_CONFIG(tooltip)
        self.txt_monitor.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.my_button.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"VENUES & EVENTS", None))
#if QT_CONFIG(tooltip)
        self.lb_homebase.setToolTip(QCoreApplication.translate("MainWindow", u"Homebase\n"
"Bla", None))
#endif // QT_CONFIG(tooltip)
        self.lb_homebase.setText(QCoreApplication.translate("MainWindow", u"Homebase City", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Venue / Event", None))
        self.field_venue_name.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.bt_venue_search_shows.setToolTip(QCoreApplication.translate("MainWindow", u"Search Shows with this Venue/Event\n"
"(click again to go back to search)", None))
#endif // QT_CONFIG(tooltip)
        self.bt_venue_search_shows.setText(QCoreApplication.translate("MainWindow", u"Shows", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.field_venue_city.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Country", None))
        self.field_venue_country.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Address", None))
#if QT_CONFIG(tooltip)
        self.bt_venue_locate.setToolTip(QCoreApplication.translate("MainWindow", u"Locate this Address on the web", None))
#endif // QT_CONFIG(tooltip)
        self.bt_venue_locate.setText(QCoreApplication.translate("MainWindow", u"Locate", None))
#if QT_CONFIG(tooltip)
        self.bt_venue_route.setToolTip(QCoreApplication.translate("MainWindow", u"Show Route to this Address on the web", None))
#endif // QT_CONFIG(tooltip)
        self.bt_venue_route.setText(QCoreApplication.translate("MainWindow", u"Route", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Geo-Coordinates", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Is an Event", None))
#if QT_CONFIG(tooltip)
        self.field_checkbox_venue_is_event.setToolTip(QCoreApplication.translate("MainWindow", u"This is an Event (Festival, Open-Air, Congress, ...)", None))
#endif // QT_CONFIG(tooltip)
        self.field_checkbox_venue_is_event.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Event Dates", None))
        self.field_venue_start_dateedit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.field_venue_end_dateedit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Website", None))
#if QT_CONFIG(tooltip)
        self.bt_website.setToolTip(QCoreApplication.translate("MainWindow", u"Open this Website", None))
#endif // QT_CONFIG(tooltip)
        self.bt_website.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Genres", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Rating", None))
#if QT_CONFIG(tooltip)
        self.cb_venue_rating.setToolTip(QCoreApplication.translate("MainWindow", u"Rating (none = no rating)", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Discontinued", None))
#if QT_CONFIG(tooltip)
        self.field_checkbox_venue_is_discontinued.setToolTip(QCoreApplication.translate("MainWindow", u"Venue/Event is discontinued", None))
#endif // QT_CONFIG(tooltip)
        self.field_checkbox_venue_is_discontinued.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Venue Info", None))
        self.tagsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
#if QT_CONFIG(tooltip)
        self.field_venue_tags.setToolTip(QCoreApplication.translate("MainWindow", u"E.g. #great-host, #black-list", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.field_venue_geocoordinates.setToolTip(QCoreApplication.translate("MainWindow", u"Lat, Lon (dec). E.g.: 47.994853, 7.843950", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bt_venue_locate_geocoordinates.setToolTip(QCoreApplication.translate("MainWindow", u"Locate these Geo-Coordinates on the web", None))
#endif // QT_CONFIG(tooltip)
        self.bt_venue_locate_geocoordinates.setText(QCoreApplication.translate("MainWindow", u"Locate", None))
#if QT_CONFIG(tooltip)
        self.bt_save_venue.setToolTip(QCoreApplication.translate("MainWindow", u"Save current Venue/Event", None))
#endif // QT_CONFIG(tooltip)
        self.bt_save_venue.setText(QCoreApplication.translate("MainWindow", u"Save Venue", None))
#if QT_CONFIG(tooltip)
        self.bt_new_venue.setToolTip(QCoreApplication.translate("MainWindow", u"Add a new Venue/Event", None))
#endif // QT_CONFIG(tooltip)
        self.bt_new_venue.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
#if QT_CONFIG(tooltip)
        self.bt_delete_venue.setToolTip(QCoreApplication.translate("MainWindow", u"Delete current Venue/Event", None))
#endif // QT_CONFIG(tooltip)
        self.bt_delete_venue.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.menuDatabases.setTitle(QCoreApplication.translate("MainWindow", u"Databases", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
        self.menuFolders.setTitle(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi


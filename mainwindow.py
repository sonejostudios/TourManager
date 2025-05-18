# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1814, 1000)
        self.actionBackup = QAction(MainWindow)
        self.actionBackup.setObjectName(u"actionBackup")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionFuture_Shows = QAction(MainWindow)
        self.actionFuture_Shows.setObjectName(u"actionFuture_Shows")
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_16 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.shows_panel = QFrame(self.centralwidget)
        self.shows_panel.setObjectName(u"shows_panel")
        self.shows_panel.setMinimumSize(QSize(430, 0))
        self.shows_panel.setMaximumSize(QSize(430, 16777215))
        self.shows_panel.setFrameShape(QFrame.Shape.NoFrame)
        self.shows_panel.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.shows_panel)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_shows_title = QLabel(self.shows_panel)
        self.lb_shows_title.setObjectName(u"lb_shows_title")
        self.lb_shows_title.setMinimumSize(QSize(0, 0))
        self.lb_shows_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lb_shows_title)

        self.show_fields = QFrame(self.shows_panel)
        self.show_fields.setObjectName(u"show_fields")
        self.show_fields.setFrameShape(QFrame.Shape.NoFrame)
        self.show_fields.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.show_fields)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.show_fields)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.field_show_dateedit = QDateEdit(self.show_fields)
        self.field_show_dateedit.setObjectName(u"field_show_dateedit")
        self.field_show_dateedit.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.field_show_dateedit)

        self.lb_show_weekday = QLabel(self.show_fields)
        self.lb_show_weekday.setObjectName(u"lb_show_weekday")
        self.lb_show_weekday.setMinimumSize(QSize(26, 0))
        self.lb_show_weekday.setMaximumSize(QSize(26, 16777215))
        self.lb_show_weekday.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_show_weekday)

        self.field_show_show_id = QLineEdit(self.show_fields)
        self.field_show_show_id.setObjectName(u"field_show_show_id")
        self.field_show_show_id.setMaximumSize(QSize(36, 16777215))
        self.field_show_show_id.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.field_show_show_id)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_29 = QLabel(self.show_fields)
        self.label_29.setObjectName(u"label_29")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_29)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.field_show_venue_text = QLineEdit(self.show_fields)
        self.field_show_venue_text.setObjectName(u"field_show_venue_text")
        self.field_show_venue_text.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.field_show_venue_text)

        self.bt_assign_venue_to_show = QPushButton(self.show_fields)
        self.bt_assign_venue_to_show.setObjectName(u"bt_assign_venue_to_show")
        self.bt_assign_venue_to_show.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.bt_assign_venue_to_show)

        self.field_show_venue_id = QLineEdit(self.show_fields)
        self.field_show_venue_id.setObjectName(u"field_show_venue_id")
        self.field_show_venue_id.setMaximumSize(QSize(36, 16777215))
        self.field_show_venue_id.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.field_show_venue_id)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_24 = QLabel(self.show_fields)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.cb_show_status = QComboBox(self.show_fields)
        self.cb_show_status.setObjectName(u"cb_show_status")
        self.cb_show_status.setMinimumSize(QSize(0, 0))
        self.cb_show_status.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_show_status)

        self.label = QLabel(self.show_fields)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label)

        self.label_15 = QLabel(self.show_fields)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_15)

        self.field_show_contact = QLineEdit(self.show_fields)
        self.field_show_contact.setObjectName(u"field_show_contact")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.field_show_contact)

        self.label_16 = QLabel(self.show_fields)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_16)

        self.field_show_phone = QLineEdit(self.show_fields)
        self.field_show_phone.setObjectName(u"field_show_phone")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.field_show_phone)

        self.label_17 = QLabel(self.show_fields)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.show_fields)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_18)

        self.field_show_tech_contact = QLineEdit(self.show_fields)
        self.field_show_tech_contact.setObjectName(u"field_show_tech_contact")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.field_show_tech_contact)

        self.label_19 = QLabel(self.show_fields)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_19)

        self.field_show_tech_phone = QLineEdit(self.show_fields)
        self.field_show_tech_phone.setObjectName(u"field_show_tech_phone")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.field_show_tech_phone)

        self.label_20 = QLabel(self.show_fields)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_20)

        self.field_show_tech_email = QLineEdit(self.show_fields)
        self.field_show_tech_email.setObjectName(u"field_show_tech_email")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.field_show_tech_email)

        self.label_25 = QLabel(self.show_fields)
        self.label_25.setObjectName(u"label_25")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_25)

        self.bt_show_folder = QPushButton(self.show_fields)
        self.bt_show_folder.setObjectName(u"bt_show_folder")
        self.bt_show_folder.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.bt_show_folder)

        self.arrivalTimeLabel = QLabel(self.show_fields)
        self.arrivalTimeLabel.setObjectName(u"arrivalTimeLabel")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.arrivalTimeLabel)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.field_show_arrival_time = QLineEdit(self.show_fields)
        self.field_show_arrival_time.setObjectName(u"field_show_arrival_time")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.field_show_arrival_time.sizePolicy().hasHeightForWidth())
        self.field_show_arrival_time.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.field_show_arrival_time, 1, 1, 1, 1)

        self.label_30 = QLabel(self.show_fields)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_30, 0, 1, 1, 1)

        self.label_22 = QLabel(self.show_fields)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_22, 0, 2, 1, 1)

        self.field_show_soundcheck_time = QLineEdit(self.show_fields)
        self.field_show_soundcheck_time.setObjectName(u"field_show_soundcheck_time")
        sizePolicy1.setHeightForWidth(self.field_show_soundcheck_time.sizePolicy().hasHeightForWidth())
        self.field_show_soundcheck_time.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.field_show_soundcheck_time, 1, 2, 1, 1)

        self.label_31 = QLabel(self.show_fields)
        self.label_31.setObjectName(u"label_31")
        sizePolicy2.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_31, 2, 1, 1, 1)

        self.field_show_opening_time = QLineEdit(self.show_fields)
        self.field_show_opening_time.setObjectName(u"field_show_opening_time")
        sizePolicy1.setHeightForWidth(self.field_show_opening_time.sizePolicy().hasHeightForWidth())
        self.field_show_opening_time.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.field_show_opening_time, 3, 1, 1, 1)

        self.label_26 = QLabel(self.show_fields)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_26, 2, 2, 1, 1)

        self.field_show_show_time = QLineEdit(self.show_fields)
        self.field_show_show_time.setObjectName(u"field_show_show_time")
        sizePolicy1.setHeightForWidth(self.field_show_show_time.sizePolicy().hasHeightForWidth())
        self.field_show_show_time.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.field_show_show_time, 3, 2, 1, 1)


        self.formLayout.setLayout(11, QFormLayout.FieldRole, self.gridLayout)

        self.label_23 = QLabel(self.show_fields)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_23)

        self.field_show_info = QPlainTextEdit(self.show_fields)
        self.field_show_info.setObjectName(u"field_show_info")
        sizePolicy.setHeightForWidth(self.field_show_info.sizePolicy().hasHeightForWidth())
        self.field_show_info.setSizePolicy(sizePolicy)
        self.field_show_info.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.field_show_info)

        self.label_21 = QLabel(self.show_fields)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_21)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.field_show_fee = QDoubleSpinBox(self.show_fields)
        self.field_show_fee.setObjectName(u"field_show_fee")
        self.field_show_fee.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.field_show_fee.setMaximum(99999.000000000000000)

        self.horizontalLayout_5.addWidget(self.field_show_fee)

        self.label_5 = QLabel(self.show_fields)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.field_show_travel_costs = QDoubleSpinBox(self.show_fields)
        self.field_show_travel_costs.setObjectName(u"field_show_travel_costs")
        self.field_show_travel_costs.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.field_show_travel_costs.setMaximum(99999.000000000000000)

        self.horizontalLayout_5.addWidget(self.field_show_travel_costs)

        self.label_8 = QLabel(self.show_fields)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.field_show_fee_sum = QDoubleSpinBox(self.show_fields)
        self.field_show_fee_sum.setObjectName(u"field_show_fee_sum")
        self.field_show_fee_sum.setReadOnly(True)
        self.field_show_fee_sum.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.field_show_fee_sum.setMaximum(99999.000000000000000)

        self.horizontalLayout_5.addWidget(self.field_show_fee_sum)

        self.field_show_currency = QComboBox(self.show_fields)
        self.field_show_currency.setObjectName(u"field_show_currency")
        self.field_show_currency.setEditable(True)
        self.field_show_currency.setMaxVisibleItems(20)

        self.horizontalLayout_5.addWidget(self.field_show_currency)


        self.formLayout.setLayout(13, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.accomodationLabel_2 = QLabel(self.show_fields)
        self.accomodationLabel_2.setObjectName(u"accomodationLabel_2")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.accomodationLabel_2)

        self.field_show_food_drinks = QLineEdit(self.show_fields)
        self.field_show_food_drinks.setObjectName(u"field_show_food_drinks")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.field_show_food_drinks)

        self.accomodationLabel = QLabel(self.show_fields)
        self.accomodationLabel.setObjectName(u"accomodationLabel")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.accomodationLabel)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.field_show_accomodation = QLineEdit(self.show_fields)
        self.field_show_accomodation.setObjectName(u"field_show_accomodation")

        self.horizontalLayout_8.addWidget(self.field_show_accomodation)

        self.field_show_breakfast = QLineEdit(self.show_fields)
        self.field_show_breakfast.setObjectName(u"field_show_breakfast")

        self.horizontalLayout_8.addWidget(self.field_show_breakfast)


        self.formLayout.setLayout(15, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.printLabel = QLabel(self.show_fields)
        self.printLabel.setObjectName(u"printLabel")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.printLabel)

        self.field_show_print = QLineEdit(self.show_fields)
        self.field_show_print.setObjectName(u"field_show_print")

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.field_show_print)

        self.addressForPrintLabel = QLabel(self.show_fields)
        self.addressForPrintLabel.setObjectName(u"addressForPrintLabel")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.addressForPrintLabel)

        self.field_show_print_address = QPlainTextEdit(self.show_fields)
        self.field_show_print_address.setObjectName(u"field_show_print_address")
        self.field_show_print_address.setMaximumSize(QSize(16777215, 60))

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.field_show_print_address)

        self.tagsLabel = QLabel(self.show_fields)
        self.tagsLabel.setObjectName(u"tagsLabel")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.tagsLabel)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.field_show_email = QLineEdit(self.show_fields)
        self.field_show_email.setObjectName(u"field_show_email")

        self.horizontalLayout_19.addWidget(self.field_show_email)

        self.cb_show_contact_email_hide = QCheckBox(self.show_fields)
        self.cb_show_contact_email_hide.setObjectName(u"cb_show_contact_email_hide")

        self.horizontalLayout_19.addWidget(self.cb_show_contact_email_hide)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_19)

        self.field_show_artists = QComboBox(self.show_fields)
        self.field_show_artists.setObjectName(u"field_show_artists")
        self.field_show_artists.setEditable(True)
        self.field_show_artists.setMaxVisibleItems(20)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.field_show_artists)

        self.field_show_cb_tags = QComboBox(self.show_fields)
        self.field_show_cb_tags.setObjectName(u"field_show_cb_tags")
        self.field_show_cb_tags.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.field_show_cb_tags.setEditable(True)
        self.field_show_cb_tags.setMaxVisibleItems(20)

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.field_show_cb_tags)


        self.verticalLayout_5.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.show_fields)

        self.bt_save_show = QPushButton(self.shows_panel)
        self.bt_save_show.setObjectName(u"bt_save_show")
        self.bt_save_show.setMinimumSize(QSize(0, 31))
        self.bt_save_show.setMaximumSize(QSize(16777215, 16777215))
        self.bt_save_show.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.bt_save_show.setFlat(False)

        self.verticalLayout_2.addWidget(self.bt_save_show)


        self.horizontalLayout_16.addWidget(self.shows_panel)

        self.lists_monitor = QFrame(self.centralwidget)
        self.lists_monitor.setObjectName(u"lists_monitor")
        sizePolicy.setHeightForWidth(self.lists_monitor.sizePolicy().hasHeightForWidth())
        self.lists_monitor.setSizePolicy(sizePolicy)
        self.lists_monitor.setFrameShape(QFrame.Shape.NoFrame)
        self.lists_monitor.setLineWidth(1)
        self.lists_monitor_layout = QVBoxLayout(self.lists_monitor)
        self.lists_monitor_layout.setSpacing(6)
        self.lists_monitor_layout.setObjectName(u"lists_monitor_layout")
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.lists_monitor_layout.addItem(self.verticalSpacer)

        self.splitter = QSplitter(self.lists_monitor)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.setHandleWidth(6)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.cb_search_shows = QComboBox(self.layoutWidget)
        self.cb_search_shows.setObjectName(u"cb_search_shows")
        sizePolicy1.setHeightForWidth(self.cb_search_shows.sizePolicy().hasHeightForWidth())
        self.cb_search_shows.setSizePolicy(sizePolicy1)
        self.cb_search_shows.setMinimumSize(QSize(160, 31))
        self.cb_search_shows.setEditable(True)
        self.cb_search_shows.setMaxVisibleItems(22)
        self.cb_search_shows.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.horizontalLayout_12.addWidget(self.cb_search_shows)

        self.cb_show_status_filter = QComboBox(self.layoutWidget)
        self.cb_show_status_filter.setObjectName(u"cb_show_status_filter")
        self.cb_show_status_filter.setMinimumSize(QSize(160, 31))

        self.horizontalLayout_12.addWidget(self.cb_show_status_filter)

        self.label_show_amount = QLabel(self.layoutWidget)
        self.label_show_amount.setObjectName(u"label_show_amount")
        self.label_show_amount.setMinimumSize(QSize(33, 0))
        self.label_show_amount.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_12.addWidget(self.label_show_amount)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.list_show = QListWidget(self.layoutWidget)
        self.list_show.setObjectName(u"list_show")

        self.verticalLayout_3.addWidget(self.list_show)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.bt_new_show = QPushButton(self.layoutWidget)
        self.bt_new_show.setObjectName(u"bt_new_show")
        self.bt_new_show.setMinimumSize(QSize(0, 0))
        self.bt_new_show.setFlat(False)

        self.horizontalLayout_10.addWidget(self.bt_new_show)

        self.bt_duplicate_show = QPushButton(self.layoutWidget)
        self.bt_duplicate_show.setObjectName(u"bt_duplicate_show")
        self.bt_duplicate_show.setMinimumSize(QSize(0, 0))
        self.bt_duplicate_show.setFlat(False)

        self.horizontalLayout_10.addWidget(self.bt_duplicate_show)

        self.bt_delete_show = QPushButton(self.layoutWidget)
        self.bt_delete_show.setObjectName(u"bt_delete_show")
        self.bt_delete_show.setMinimumSize(QSize(0, 0))
        self.bt_delete_show.setFlat(False)

        self.horizontalLayout_10.addWidget(self.bt_delete_show)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.cb_monitor = QComboBox(self.layoutWidget)
        self.cb_monitor.setObjectName(u"cb_monitor")
        self.cb_monitor.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_18.addWidget(self.cb_monitor)

        self.bt_monitor_menu = QToolButton(self.layoutWidget)
        self.bt_monitor_menu.setObjectName(u"bt_monitor_menu")
        self.bt_monitor_menu.setMinimumSize(QSize(0, 31))
        self.bt_monitor_menu.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        self.horizontalLayout_18.addWidget(self.bt_monitor_menu)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_15.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.cb_search_venues = QComboBox(self.layoutWidget)
        self.cb_search_venues.setObjectName(u"cb_search_venues")
        sizePolicy1.setHeightForWidth(self.cb_search_venues.sizePolicy().hasHeightForWidth())
        self.cb_search_venues.setSizePolicy(sizePolicy1)
        self.cb_search_venues.setMinimumSize(QSize(160, 31))
        self.cb_search_venues.setEditable(True)
        self.cb_search_venues.setMaxVisibleItems(22)
        self.cb_search_venues.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.horizontalLayout_13.addWidget(self.cb_search_venues)

        self.cb_venue_filter = QComboBox(self.layoutWidget)
        self.cb_venue_filter.setObjectName(u"cb_venue_filter")
        self.cb_venue_filter.setMinimumSize(QSize(160, 31))

        self.horizontalLayout_13.addWidget(self.cb_venue_filter)

        self.label_venue_amount = QLabel(self.layoutWidget)
        self.label_venue_amount.setObjectName(u"label_venue_amount")
        self.label_venue_amount.setMinimumSize(QSize(33, 0))
        self.label_venue_amount.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_13.addWidget(self.label_venue_amount)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.list_venue = QListWidget(self.layoutWidget)
        self.list_venue.setObjectName(u"list_venue")

        self.verticalLayout_4.addWidget(self.list_venue)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.bt_new_venue = QPushButton(self.layoutWidget)
        self.bt_new_venue.setObjectName(u"bt_new_venue")
        self.bt_new_venue.setMinimumSize(QSize(0, 0))
        self.bt_new_venue.setFlat(False)

        self.horizontalLayout_9.addWidget(self.bt_new_venue)

        self.bt_delete_venue = QPushButton(self.layoutWidget)
        self.bt_delete_venue.setObjectName(u"bt_delete_venue")
        self.bt_delete_venue.setMinimumSize(QSize(0, 0))
        self.bt_delete_venue.setFlat(False)

        self.horizontalLayout_9.addWidget(self.bt_delete_venue)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.bt_map = QPushButton(self.layoutWidget)
        self.bt_map.setObjectName(u"bt_map")
        self.bt_map.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_14.addWidget(self.bt_map)

        self.bt_calculator = QPushButton(self.layoutWidget)
        self.bt_calculator.setObjectName(u"bt_calculator")
        self.bt_calculator.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_14.addWidget(self.bt_calculator)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_15.addLayout(self.verticalLayout_4)

        self.splitter.addWidget(self.layoutWidget)
        self.txt_monitor = QPlainTextEdit(self.splitter)
        self.txt_monitor.setObjectName(u"txt_monitor")
        self.splitter.addWidget(self.txt_monitor)

        self.lists_monitor_layout.addWidget(self.splitter)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.table_show = QTableWidget(self.lists_monitor)
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

        self.my_button = QPushButton(self.lists_monitor)
        self.my_button.setObjectName(u"my_button")

        self.horizontalLayout_11.addWidget(self.my_button)


        self.lists_monitor_layout.addLayout(self.horizontalLayout_11)

        self.lists_monitor_layout.setStretch(1, 10)

        self.horizontalLayout_16.addWidget(self.lists_monitor)

        self.venues_panel = QFrame(self.centralwidget)
        self.venues_panel.setObjectName(u"venues_panel")
        self.venues_panel.setMinimumSize(QSize(430, 0))
        self.venues_panel.setMaximumSize(QSize(430, 16777215))
        self.venues_panel.setFrameShape(QFrame.Shape.NoFrame)
        self.venues_panel.setLineWidth(1)
        self.verticalLayout_6 = QVBoxLayout(self.venues_panel)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_venues_title = QLabel(self.venues_panel)
        self.lb_venues_title.setObjectName(u"lb_venues_title")
        self.lb_venues_title.setMinimumSize(QSize(0, 0))
        self.lb_venues_title.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lb_venues_title)

        self.lb_homebase = QLabel(self.venues_panel)
        self.lb_homebase.setObjectName(u"lb_homebase")
        self.lb_homebase.setMinimumSize(QSize(0, 30))
        self.lb_homebase.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lb_homebase)

        self.venue_fields = QFrame(self.venues_panel)
        self.venue_fields.setObjectName(u"venue_fields")
        self.venue_fields.setFrameShape(QFrame.Shape.NoFrame)
        self.venue_fields.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.venue_fields)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.venue_fields)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.field_venue_name = QLineEdit(self.venue_fields)
        self.field_venue_name.setObjectName(u"field_venue_name")

        self.horizontalLayout_7.addWidget(self.field_venue_name)

        self.bt_venue_search_shows = QPushButton(self.venue_fields)
        self.bt_venue_search_shows.setObjectName(u"bt_venue_search_shows")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bt_venue_search_shows.sizePolicy().hasHeightForWidth())
        self.bt_venue_search_shows.setSizePolicy(sizePolicy3)
        self.bt_venue_search_shows.setMinimumSize(QSize(0, 12))
        self.bt_venue_search_shows.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.bt_venue_search_shows)

        self.field_venue_venue_id = QLineEdit(self.venue_fields)
        self.field_venue_venue_id.setObjectName(u"field_venue_venue_id")
        self.field_venue_venue_id.setMaximumSize(QSize(36, 16777215))
        self.field_venue_venue_id.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.field_venue_venue_id)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_3 = QLabel(self.venue_fields)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_6 = QLabel(self.venue_fields)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.venue_fields)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.field_venue_address = QPlainTextEdit(self.venue_fields)
        self.field_venue_address.setObjectName(u"field_venue_address")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.field_venue_address.sizePolicy().hasHeightForWidth())
        self.field_venue_address.setSizePolicy(sizePolicy4)
        self.field_venue_address.setMinimumSize(QSize(0, 60))
        self.field_venue_address.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout.addWidget(self.field_venue_address)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bt_venue_locate = QPushButton(self.venue_fields)
        self.bt_venue_locate.setObjectName(u"bt_venue_locate")
        self.bt_venue_locate.setMinimumSize(QSize(0, 0))
        self.bt_venue_locate.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.bt_venue_locate)

        self.bt_venue_route = QPushButton(self.venue_fields)
        self.bt_venue_route.setObjectName(u"bt_venue_route")
        self.bt_venue_route.setMinimumSize(QSize(60, 0))
        self.bt_venue_route.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.bt_venue_route)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_32 = QLabel(self.venue_fields)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_32)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.field_venue_geocoordinates = QLineEdit(self.venue_fields)
        self.field_venue_geocoordinates.setObjectName(u"field_venue_geocoordinates")

        self.horizontalLayout_17.addWidget(self.field_venue_geocoordinates)

        self.bt_venue_locate_geocoordinates = QPushButton(self.venue_fields)
        self.bt_venue_locate_geocoordinates.setObjectName(u"bt_venue_locate_geocoordinates")
        self.bt_venue_locate_geocoordinates.setMinimumSize(QSize(0, 0))
        self.bt_venue_locate_geocoordinates.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_17.addWidget(self.bt_venue_locate_geocoordinates)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_17)

        self.label_28 = QLabel(self.venue_fields)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_28)

        self.field_checkbox_venue_is_event = QCheckBox(self.venue_fields)
        self.field_checkbox_venue_is_event.setObjectName(u"field_checkbox_venue_is_event")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.field_checkbox_venue_is_event)

        self.label_14 = QLabel(self.venue_fields)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_14)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.field_venue_start_dateedit = QDateEdit(self.venue_fields)
        self.field_venue_start_dateedit.setObjectName(u"field_venue_start_dateedit")
        self.field_venue_start_dateedit.setMinimumDate(QDate(1752, 9, 14))
        self.field_venue_start_dateedit.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.field_venue_start_dateedit)

        self.lb_venue_eventstart_weekday = QLabel(self.venue_fields)
        self.lb_venue_eventstart_weekday.setObjectName(u"lb_venue_eventstart_weekday")
        self.lb_venue_eventstart_weekday.setMinimumSize(QSize(26, 0))
        self.lb_venue_eventstart_weekday.setMaximumSize(QSize(26, 16777215))
        self.lb_venue_eventstart_weekday.setFrameShadow(QFrame.Shadow.Sunken)
        self.lb_venue_eventstart_weekday.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_venue_eventstart_weekday)

        self.lb_venue_event_arrow = QLabel(self.venue_fields)
        self.lb_venue_event_arrow.setObjectName(u"lb_venue_event_arrow")
        self.lb_venue_event_arrow.setMinimumSize(QSize(20, 0))
        self.lb_venue_event_arrow.setMaximumSize(QSize(20, 16777215))
        self.lb_venue_event_arrow.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lb_venue_event_arrow)

        self.lb_venue_eventend_weekday = QLabel(self.venue_fields)
        self.lb_venue_eventend_weekday.setObjectName(u"lb_venue_eventend_weekday")
        self.lb_venue_eventend_weekday.setMinimumSize(QSize(26, 0))
        self.lb_venue_eventend_weekday.setMaximumSize(QSize(26, 16777215))
        self.lb_venue_eventend_weekday.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lb_venue_eventend_weekday)

        self.field_venue_end_dateedit = QDateEdit(self.venue_fields)
        self.field_venue_end_dateedit.setObjectName(u"field_venue_end_dateedit")
        self.field_venue_end_dateedit.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.field_venue_end_dateedit)


        self.formLayout_2.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.label_9 = QLabel(self.venue_fields)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.field_venue_website = QLineEdit(self.venue_fields)
        self.field_venue_website.setObjectName(u"field_venue_website")

        self.horizontalLayout_2.addWidget(self.field_venue_website)

        self.bt_website = QPushButton(self.venue_fields)
        self.bt_website.setObjectName(u"bt_website")
        self.bt_website.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.bt_website)


        self.formLayout_2.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_33 = QLabel(self.venue_fields)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_33)

        self.field_venue_genres = QLineEdit(self.venue_fields)
        self.field_venue_genres.setObjectName(u"field_venue_genres")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.field_venue_genres)

        self.label_37 = QLabel(self.venue_fields)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_37)

        self.field_venue_capacity = QLineEdit(self.venue_fields)
        self.field_venue_capacity.setObjectName(u"field_venue_capacity")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.field_venue_capacity)

        self.label_35 = QLabel(self.venue_fields)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_35)

        self.cb_venue_rating = QComboBox(self.venue_fields)
        self.cb_venue_rating.setObjectName(u"cb_venue_rating")
        self.cb_venue_rating.setMinimumSize(QSize(0, 0))
        self.cb_venue_rating.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.cb_venue_rating.setFont(font)
        self.cb_venue_rating.setFrame(True)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.cb_venue_rating)

        self.label_27 = QLabel(self.venue_fields)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.label_27)

        self.field_checkbox_venue_is_discontinued = QCheckBox(self.venue_fields)
        self.field_checkbox_venue_is_discontinued.setObjectName(u"field_checkbox_venue_is_discontinued")

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.field_checkbox_venue_is_discontinued)

        self.label_11 = QLabel(self.venue_fields)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_11)

        self.field_venue_contact = QLineEdit(self.venue_fields)
        self.field_venue_contact.setObjectName(u"field_venue_contact")

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.field_venue_contact)

        self.label_12 = QLabel(self.venue_fields)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.label_12)

        self.field_venue_phone = QLineEdit(self.venue_fields)
        self.field_venue_phone.setObjectName(u"field_venue_phone")

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.field_venue_phone)

        self.label_13 = QLabel(self.venue_fields)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.label_13)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.field_venue_email = QLineEdit(self.venue_fields)
        self.field_venue_email.setObjectName(u"field_venue_email")

        self.horizontalLayout_20.addWidget(self.field_venue_email)

        self.cb_venue_contact_email_hide = QCheckBox(self.venue_fields)
        self.cb_venue_contact_email_hide.setObjectName(u"cb_venue_contact_email_hide")

        self.horizontalLayout_20.addWidget(self.cb_venue_contact_email_hide)


        self.formLayout_2.setLayout(14, QFormLayout.FieldRole, self.horizontalLayout_20)

        self.label_10 = QLabel(self.venue_fields)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(15, QFormLayout.LabelRole, self.label_10)

        self.field_venue_info = QPlainTextEdit(self.venue_fields)
        self.field_venue_info.setObjectName(u"field_venue_info")

        self.formLayout_2.setWidget(15, QFormLayout.FieldRole, self.field_venue_info)

        self.tagsLabel_2 = QLabel(self.venue_fields)
        self.tagsLabel_2.setObjectName(u"tagsLabel_2")

        self.formLayout_2.setWidget(17, QFormLayout.LabelRole, self.tagsLabel_2)

        self.field_venue_country = QComboBox(self.venue_fields)
        self.field_venue_country.setObjectName(u"field_venue_country")
        self.field_venue_country.setEditable(True)
        self.field_venue_country.setMaxVisibleItems(20)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.field_venue_country)

        self.field_venue_city = QComboBox(self.venue_fields)
        self.field_venue_city.setObjectName(u"field_venue_city")
        self.field_venue_city.setEditable(True)
        self.field_venue_city.setMaxVisibleItems(20)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.field_venue_city)

        self.field_venue_cb_tags = QComboBox(self.venue_fields)
        self.field_venue_cb_tags.setObjectName(u"field_venue_cb_tags")
        self.field_venue_cb_tags.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.field_venue_cb_tags.setEditable(True)
        self.field_venue_cb_tags.setMaxVisibleItems(20)

        self.formLayout_2.setWidget(17, QFormLayout.FieldRole, self.field_venue_cb_tags)


        self.verticalLayout_7.addLayout(self.formLayout_2)


        self.verticalLayout_6.addWidget(self.venue_fields)

        self.bt_save_venue = QPushButton(self.venues_panel)
        self.bt_save_venue.setObjectName(u"bt_save_venue")
        self.bt_save_venue.setMinimumSize(QSize(0, 31))
        self.bt_save_venue.setFlat(False)

        self.verticalLayout_6.addWidget(self.bt_save_venue)


        self.horizontalLayout_16.addWidget(self.venues_panel)

        self.horizontalLayout_16.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1814, 20))
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
        self.menuCustom_Links = QMenu(self.menubar)
        self.menuCustom_Links.setObjectName(u"menuCustom_Links")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatabases.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuFolders.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuCustom_Links.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuDatabases.addAction(self.actionBackup)
        self.menuDatabases.addSeparator()
        self.menuDatabases.addAction(self.actionQuit)
        self.menuExport.addAction(self.actionFuture_Shows)
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
        self.actionFuture_Shows.setText(QCoreApplication.translate("MainWindow", u"Future Shows (.html)", None))
        self.actionCalendars.setText(QCoreApplication.translate("MainWindow", u"Calendars (.ics)", None))
        self.actionOpen_Working_Folder.setText(QCoreApplication.translate("MainWindow", u"Working Folder", None))
        self.actionOpen_Show_Folder.setText(QCoreApplication.translate("MainWindow", u"Shows", None))
        self.actionOpen_Backup_Folder.setText(QCoreApplication.translate("MainWindow", u"Backups", None))
        self.actionOpen_Root_Folder.setText(QCoreApplication.translate("MainWindow", u"Application Folder", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionTravel_Costs_Calculator.setText(QCoreApplication.translate("MainWindow", u"Travel Costs Calculator", None))
        self.actionMap.setText(QCoreApplication.translate("MainWindow", u"Map", None))
        self.lb_shows_title.setText(QCoreApplication.translate("MainWindow", u"SHOWS", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Date", None))
#if QT_CONFIG(tooltip)
        self.field_show_dateedit.setToolTip(QCoreApplication.translate("MainWindow", u"The show's date", None))
#endif // QT_CONFIG(tooltip)
        self.field_show_dateedit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.lb_show_weekday.setText(QCoreApplication.translate("MainWindow", u"Day", None))
#if QT_CONFIG(tooltip)
        self.field_show_show_id.setToolTip(QCoreApplication.translate("MainWindow", u"ShowID", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Venue", None))
#if QT_CONFIG(tooltip)
        self.field_show_venue_text.setToolTip(QCoreApplication.translate("MainWindow", u"The venue's city and name\n"
"Use the venue list to change it", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bt_assign_venue_to_show.setToolTip(QCoreApplication.translate("MainWindow", u"Assign the selected venue to the selected show\n"
"(or double-click on venue)", None))
#endif // QT_CONFIG(tooltip)
        self.bt_assign_venue_to_show.setText(QCoreApplication.translate("MainWindow", u"Assign Venue", None))
#if QT_CONFIG(tooltip)
        self.field_show_venue_id.setToolTip(QCoreApplication.translate("MainWindow", u"VenueID", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.field_show_venue_id.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.field_show_venue_id.setPlaceholderText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Booking Status", None))
#if QT_CONFIG(tooltip)
        self.cb_show_status.setToolTip(QCoreApplication.translate("MainWindow", u"Current booking status", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
#if QT_CONFIG(tooltip)
        self.field_show_contact.setToolTip(QCoreApplication.translate("MainWindow", u"Contact person for this show", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
#if QT_CONFIG(tooltip)
        self.field_show_phone.setToolTip(QCoreApplication.translate("MainWindow", u"Phone number of the contact person", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Technician", None))
#if QT_CONFIG(tooltip)
        self.field_show_tech_contact.setToolTip(QCoreApplication.translate("MainWindow", u"Name of the main technician", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Tech Phone", None))
#if QT_CONFIG(tooltip)
        self.field_show_tech_phone.setToolTip(QCoreApplication.translate("MainWindow", u"Phone of the main techncian", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tech Email", None))
#if QT_CONFIG(tooltip)
        self.field_show_tech_email.setToolTip(QCoreApplication.translate("MainWindow", u"Email address of the main technician", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Show Folder", None))
#if QT_CONFIG(tooltip)
        self.bt_show_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Create or open Show Folder", None))
#endif // QT_CONFIG(tooltip)
        self.bt_show_folder.setText(QCoreApplication.translate("MainWindow", u"Show Folder", None))
        self.arrivalTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
#if QT_CONFIG(tooltip)
        self.field_show_arrival_time.setToolTip(QCoreApplication.translate("MainWindow", u"Arrival time, get in time", None))
#endif // QT_CONFIG(tooltip)
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Arrival", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Technical Check", None))
#if QT_CONFIG(tooltip)
        self.field_show_soundcheck_time.setToolTip(QCoreApplication.translate("MainWindow", u"Sound check time, light check time, etc", None))
#endif // QT_CONFIG(tooltip)
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Doors Opening", None))
#if QT_CONFIG(tooltip)
        self.field_show_opening_time.setToolTip(QCoreApplication.translate("MainWindow", u"Door opening time, event starting time", None))
#endif // QT_CONFIG(tooltip)
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Show Time", None))
#if QT_CONFIG(tooltip)
        self.field_show_show_time.setToolTip(QCoreApplication.translate("MainWindow", u"Show starting time", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Fee + Travel Costs", None))
#if QT_CONFIG(tooltip)
        self.field_show_fee.setToolTip(QCoreApplication.translate("MainWindow", u"Fee", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.field_show_travel_costs.setToolTip(QCoreApplication.translate("MainWindow", u"Travel costs", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(tooltip)
        self.field_show_fee_sum.setToolTip(QCoreApplication.translate("MainWindow", u"Sum", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.field_show_currency.setToolTip(QCoreApplication.translate("MainWindow", u"Currency", None))
#endif // QT_CONFIG(tooltip)
        self.accomodationLabel_2.setText(QCoreApplication.translate("MainWindow", u"Food & Drinks", None))
#if QT_CONFIG(tooltip)
        self.field_show_food_drinks.setToolTip(QCoreApplication.translate("MainWindow", u"Food, drinks, meals, etc", None))
#endif // QT_CONFIG(tooltip)
        self.accomodationLabel.setText(QCoreApplication.translate("MainWindow", u"Bed & Breakfast", None))
#if QT_CONFIG(tooltip)
        self.field_show_accomodation.setToolTip(QCoreApplication.translate("MainWindow", u"Bed (accomodation)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.field_show_breakfast.setToolTip(QCoreApplication.translate("MainWindow", u"Breakfast", None))
#endif // QT_CONFIG(tooltip)
        self.printLabel.setText(QCoreApplication.translate("MainWindow", u"Print", None))
#if QT_CONFIG(tooltip)
        self.field_show_print.setToolTip(QCoreApplication.translate("MainWindow", u"Print material to be send (posters, amount, ...)", None))
#endif // QT_CONFIG(tooltip)
        self.addressForPrintLabel.setText(QCoreApplication.translate("MainWindow", u"Address for Print  ", None))
#if QT_CONFIG(tooltip)
        self.field_show_print_address.setToolTip(QCoreApplication.translate("MainWindow", u"Address where to send print material", None))
#endif // QT_CONFIG(tooltip)
        self.tagsLabel.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
#if QT_CONFIG(tooltip)
        self.field_show_email.setToolTip(QCoreApplication.translate("MainWindow", u"Email address of the contact person", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cb_show_contact_email_hide.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude this email address from the Monitor's email collections", None))
#endif // QT_CONFIG(tooltip)
        self.cb_show_contact_email_hide.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
#if QT_CONFIG(tooltip)
        self.field_show_artists.setToolTip(QCoreApplication.translate("MainWindow", u"Artist involved", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.field_show_cb_tags.setToolTip(QCoreApplication.translate("MainWindow", u"Show tags", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bt_save_show.setToolTip(QCoreApplication.translate("MainWindow", u"Save current Show", None))
#endif // QT_CONFIG(tooltip)
        self.bt_save_show.setText(QCoreApplication.translate("MainWindow", u"Save Show", None))
#if QT_CONFIG(tooltip)
        self.cb_search_shows.setToolTip(QCoreApplication.translate("MainWindow", u"Show search", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cb_show_status_filter.setToolTip(QCoreApplication.translate("MainWindow", u"Show Status Filter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_show_amount.setToolTip(QCoreApplication.translate("MainWindow", u"Amount of Shows in list", None))
#endif // QT_CONFIG(tooltip)
        self.label_show_amount.setText(QCoreApplication.translate("MainWindow", u"SHO", None))
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
        self.cb_monitor.setToolTip(QCoreApplication.translate("MainWindow", u"Monitor selection\n"
"Get Information according to Searches and Filters\n"
"(except Notes and Paths)", None))
#endif // QT_CONFIG(tooltip)
        self.bt_monitor_menu.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.cb_search_venues.setToolTip(QCoreApplication.translate("MainWindow", u"Show search", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cb_venue_filter.setToolTip(QCoreApplication.translate("MainWindow", u"Venue Filter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_venue_amount.setToolTip(QCoreApplication.translate("MainWindow", u"Amount of Venues in list", None))
#endif // QT_CONFIG(tooltip)
        self.label_venue_amount.setText(QCoreApplication.translate("MainWindow", u"VEN", None))
#if QT_CONFIG(tooltip)
        self.bt_new_venue.setToolTip(QCoreApplication.translate("MainWindow", u"Add a new Venue/Event", None))
#endif // QT_CONFIG(tooltip)
        self.bt_new_venue.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
#if QT_CONFIG(tooltip)
        self.bt_delete_venue.setToolTip(QCoreApplication.translate("MainWindow", u"Delete current Venue/Event", None))
#endif // QT_CONFIG(tooltip)
        self.bt_delete_venue.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
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
        self.lb_venues_title.setText(QCoreApplication.translate("MainWindow", u"VENUES & EVENTS", None))
#if QT_CONFIG(tooltip)
        self.lb_homebase.setToolTip(QCoreApplication.translate("MainWindow", u"Homebase\n"
"Bla", None))
#endif // QT_CONFIG(tooltip)
        self.lb_homebase.setText(QCoreApplication.translate("MainWindow", u"Homebase City", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Venue / Event", None))
#if QT_CONFIG(tooltip)
        self.field_venue_name.setToolTip(QCoreApplication.translate("MainWindow", u"Name of the venue/event", None))
#endif // QT_CONFIG(tooltip)
        self.field_venue_name.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.bt_venue_search_shows.setToolTip(QCoreApplication.translate("MainWindow", u"Search shows with this venue/event\n"
"(click again to go back to search)", None))
#endif // QT_CONFIG(tooltip)
        self.bt_venue_search_shows.setText(QCoreApplication.translate("MainWindow", u"Shows", None))
#if QT_CONFIG(tooltip)
        self.field_venue_venue_id.setToolTip(QCoreApplication.translate("MainWindow", u"VenueID", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.field_venue_venue_id.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.field_venue_venue_id.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Country", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Address", None))
#if QT_CONFIG(tooltip)
        self.field_venue_address.setToolTip(QCoreApplication.translate("MainWindow", u"Address of the venue/event", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bt_venue_locate.setToolTip(QCoreApplication.translate("MainWindow", u"Locate this address on the web", None))
#endif // QT_CONFIG(tooltip)
        self.bt_venue_locate.setText(QCoreApplication.translate("MainWindow", u"Locate", None))
#if QT_CONFIG(tooltip)
        self.bt_venue_route.setToolTip(QCoreApplication.translate("MainWindow", u"Show directions to this address on the web", None))
#endif // QT_CONFIG(tooltip)
        self.bt_venue_route.setText(QCoreApplication.translate("MainWindow", u"Route", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Geo-Coordinates", None))
#if QT_CONFIG(tooltip)
        self.field_venue_geocoordinates.setToolTip(QCoreApplication.translate("MainWindow", u"Latitude, longitude (dec). E.g.: 47.994853, 7.843950", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bt_venue_locate_geocoordinates.setToolTip(QCoreApplication.translate("MainWindow", u"Locate these geo-coordinates on the web", None))
#endif // QT_CONFIG(tooltip)
        self.bt_venue_locate_geocoordinates.setText(QCoreApplication.translate("MainWindow", u"Locate", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Is an Event", None))
#if QT_CONFIG(tooltip)
        self.field_checkbox_venue_is_event.setToolTip(QCoreApplication.translate("MainWindow", u"This is an Event (festival, open-Air, congress, ...)", None))
#endif // QT_CONFIG(tooltip)
        self.field_checkbox_venue_is_event.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Event Dates", None))
#if QT_CONFIG(tooltip)
        self.field_venue_start_dateedit.setToolTip(QCoreApplication.translate("MainWindow", u"Start date", None))
#endif // QT_CONFIG(tooltip)
        self.field_venue_start_dateedit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.lb_venue_eventstart_weekday.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.lb_venue_event_arrow.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u2192</p></body></html>", None))
        self.lb_venue_eventend_weekday.setText(QCoreApplication.translate("MainWindow", u"Day", None))
#if QT_CONFIG(tooltip)
        self.field_venue_end_dateedit.setToolTip(QCoreApplication.translate("MainWindow", u"End date", None))
#endif // QT_CONFIG(tooltip)
        self.field_venue_end_dateedit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Website", None))
#if QT_CONFIG(tooltip)
        self.field_venue_website.setToolTip(QCoreApplication.translate("MainWindow", u"Website of the venue/event", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bt_website.setToolTip(QCoreApplication.translate("MainWindow", u"Open this website", None))
#endif // QT_CONFIG(tooltip)
        self.bt_website.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Genres", None))
#if QT_CONFIG(tooltip)
        self.field_venue_genres.setToolTip(QCoreApplication.translate("MainWindow", u"Genres, styles", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Capacity", None))
#if QT_CONFIG(tooltip)
        self.field_venue_capacity.setToolTip(QCoreApplication.translate("MainWindow", u"Amount of people (spectators, audience)", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Rating", None))
#if QT_CONFIG(tooltip)
        self.cb_venue_rating.setToolTip(QCoreApplication.translate("MainWindow", u"Rating (none = no rating)", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Discontinued", None))
#if QT_CONFIG(tooltip)
        self.field_checkbox_venue_is_discontinued.setToolTip(QCoreApplication.translate("MainWindow", u"Venue/Event is discontinued and/or doesn't exist anymore", None))
#endif // QT_CONFIG(tooltip)
        self.field_checkbox_venue_is_discontinued.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
#if QT_CONFIG(tooltip)
        self.field_venue_contact.setToolTip(QCoreApplication.translate("MainWindow", u"Contact person of this venue/event", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
#if QT_CONFIG(tooltip)
        self.field_venue_phone.setToolTip(QCoreApplication.translate("MainWindow", u"Phone number of the contact person", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Email", None))
#if QT_CONFIG(tooltip)
        self.field_venue_email.setToolTip(QCoreApplication.translate("MainWindow", u"Email address of the contact person", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cb_venue_contact_email_hide.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude this email address from the Monitor's email collections", None))
#endif // QT_CONFIG(tooltip)
        self.cb_venue_contact_email_hide.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.field_venue_info.setPlainText("")
        self.tagsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
#if QT_CONFIG(tooltip)
        self.field_venue_country.setToolTip(QCoreApplication.translate("MainWindow", u"Country of the venue/event", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.field_venue_city.setToolTip(QCoreApplication.translate("MainWindow", u"City of the venue/event", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.field_venue_cb_tags.setToolTip(QCoreApplication.translate("MainWindow", u"Venue tags", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bt_save_venue.setToolTip(QCoreApplication.translate("MainWindow", u"Save current Venue/Event", None))
#endif // QT_CONFIG(tooltip)
        self.bt_save_venue.setText(QCoreApplication.translate("MainWindow", u"Save Venue / Event", None))
        self.menuDatabases.setTitle(QCoreApplication.translate("MainWindow", u"Databases", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
        self.menuFolders.setTitle(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuCustom_Links.setTitle(QCoreApplication.translate("MainWindow", u"Custom Links", None))
    # retranslateUi


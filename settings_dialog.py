# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(900, 600)
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.defaults = QWidget()
        self.defaults.setObjectName(u"defaults")
        self.horizontalLayout_3 = QHBoxLayout(self.defaults)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.defaults)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.homebaseCityLabel = QLabel(self.groupBox)
        self.homebaseCityLabel.setObjectName(u"homebaseCityLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.homebaseCityLabel)

        self.field_homebase_city = QLineEdit(self.groupBox)
        self.field_homebase_city.setObjectName(u"field_homebase_city")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.field_homebase_city)

        self.geocoordinatesLabel = QLabel(self.groupBox)
        self.geocoordinatesLabel.setObjectName(u"geocoordinatesLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.geocoordinatesLabel)

        self.field_geocoordinates = QLineEdit(self.groupBox)
        self.field_geocoordinates.setObjectName(u"field_geocoordinates")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.field_geocoordinates)

        self.artistLabel = QLabel(self.groupBox)
        self.artistLabel.setObjectName(u"artistLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.artistLabel)

        self.field_artist = QLineEdit(self.groupBox)
        self.field_artist.setObjectName(u"field_artist")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.field_artist)

        self.currencyLabel = QLabel(self.groupBox)
        self.currencyLabel.setObjectName(u"currencyLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.currencyLabel)

        self.field_currency = QLineEdit(self.groupBox)
        self.field_currency.setObjectName(u"field_currency")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.field_currency)

        self.distanceUnitLabel = QLabel(self.groupBox)
        self.distanceUnitLabel.setObjectName(u"distanceUnitLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.distanceUnitLabel)

        self.field_distance_unit = QLineEdit(self.groupBox)
        self.field_distance_unit.setObjectName(u"field_distance_unit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.field_distance_unit)

        self.travelUnitPriceLabel = QLabel(self.groupBox)
        self.travelUnitPriceLabel.setObjectName(u"travelUnitPriceLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.travelUnitPriceLabel)

        self.field_travel_unit_price = QDoubleSpinBox(self.groupBox)
        self.field_travel_unit_price.setObjectName(u"field_travel_unit_price")
        self.field_travel_unit_price.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.field_travel_unit_price.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.field_travel_unit_price)


        self.verticalLayout_4.addLayout(self.formLayout)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.defaults)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.themeLabel = QLabel(self.groupBox_2)
        self.themeLabel.setObjectName(u"themeLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.themeLabel)

        self.field_theme = QComboBox(self.groupBox_2)
        self.field_theme.setObjectName(u"field_theme")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.field_theme)

        self.fontSizeLabel = QLabel(self.groupBox_2)
        self.fontSizeLabel.setObjectName(u"fontSizeLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.fontSizeLabel)

        self.field_fontsize = QSpinBox(self.groupBox_2)
        self.field_fontsize.setObjectName(u"field_fontsize")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.field_fontsize)

        self.fieldAreaWidthLabel = QLabel(self.groupBox_2)
        self.fieldAreaWidthLabel.setObjectName(u"fieldAreaWidthLabel")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.fieldAreaWidthLabel)

        self.field_field_area_width = QSpinBox(self.groupBox_2)
        self.field_field_area_width.setObjectName(u"field_field_area_width")
        self.field_field_area_width.setMaximum(999)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.field_field_area_width)

        self.saveAndRestoreWindowSizeLabel = QLabel(self.groupBox_2)
        self.saveAndRestoreWindowSizeLabel.setObjectName(u"saveAndRestoreWindowSizeLabel")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.saveAndRestoreWindowSizeLabel)

        self.field_save_window_size = QCheckBox(self.groupBox_2)
        self.field_save_window_size.setObjectName(u"field_save_window_size")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.field_save_window_size)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.field_start_with_selected_show = QCheckBox(self.groupBox_2)
        self.field_start_with_selected_show.setObjectName(u"field_start_with_selected_show")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.field_start_with_selected_show)

        self.calculatorTextDecimalSeparatorLabel = QLabel(self.groupBox_2)
        self.calculatorTextDecimalSeparatorLabel.setObjectName(u"calculatorTextDecimalSeparatorLabel")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.calculatorTextDecimalSeparatorLabel)

        self.field_calc_text_decimal_separator = QComboBox(self.groupBox_2)
        self.field_calc_text_decimal_separator.setObjectName(u"field_calc_text_decimal_separator")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.field_calc_text_decimal_separator)

        self.mapProviderLabel = QLabel(self.groupBox_2)
        self.mapProviderLabel.setObjectName(u"mapProviderLabel")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.mapProviderLabel)

        self.field_map_provider = QComboBox(self.groupBox_2)
        self.field_map_provider.setObjectName(u"field_map_provider")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.FieldRole, self.field_map_provider)


        self.verticalLayout_5.addLayout(self.formLayout_2)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.defaults, "")
        self.paths_exports = QWidget()
        self.paths_exports.setObjectName(u"paths_exports")
        self.verticalLayout_7 = QVBoxLayout(self.paths_exports)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_3 = QGroupBox(self.paths_exports)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.field_workdir = QLineEdit(self.groupBox_3)
        self.field_workdir.setObjectName(u"field_workdir")

        self.horizontalLayout.addWidget(self.field_workdir)

        self.bt_select_workdir = QPushButton(self.groupBox_3)
        self.bt_select_workdir.setObjectName(u"bt_select_workdir")
        self.bt_select_workdir.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.bt_select_workdir)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.field_show_calendar_path = QLineEdit(self.groupBox_3)
        self.field_show_calendar_path.setObjectName(u"field_show_calendar_path")
        self.field_show_calendar_path.setFrame(False)
        self.field_show_calendar_path.setReadOnly(True)

        self.gridLayout.addWidget(self.field_show_calendar_path, 0, 1, 1, 1)

        self.bt_copy_show_calendar = QPushButton(self.groupBox_3)
        self.bt_copy_show_calendar.setObjectName(u"bt_copy_show_calendar")
        self.bt_copy_show_calendar.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.bt_copy_show_calendar, 0, 2, 1, 1)

        self.bt_copy_event_calendar = QPushButton(self.groupBox_3)
        self.bt_copy_event_calendar.setObjectName(u"bt_copy_event_calendar")
        self.bt_copy_event_calendar.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.bt_copy_event_calendar, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.field_event_calendar_path = QLineEdit(self.groupBox_3)
        self.field_event_calendar_path.setObjectName(u"field_event_calendar_path")
        self.field_event_calendar_path.setFrame(False)
        self.field_event_calendar_path.setReadOnly(True)

        self.gridLayout.addWidget(self.field_event_calendar_path, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.field_event_forecast_calendar_path = QLineEdit(self.groupBox_3)
        self.field_event_forecast_calendar_path.setObjectName(u"field_event_forecast_calendar_path")
        self.field_event_forecast_calendar_path.setFrame(False)
        self.field_event_forecast_calendar_path.setReadOnly(True)

        self.gridLayout.addWidget(self.field_event_forecast_calendar_path, 2, 1, 1, 1)

        self.bt_copy_event_forecast_calendar = QPushButton(self.groupBox_3)
        self.bt_copy_event_forecast_calendar.setObjectName(u"bt_copy_event_forecast_calendar")
        self.bt_copy_event_forecast_calendar.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.bt_copy_event_forecast_calendar, 2, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.paths_exports)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.autoExportFutureShowsLabel = QLabel(self.groupBox_4)
        self.autoExportFutureShowsLabel.setObjectName(u"autoExportFutureShowsLabel")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.autoExportFutureShowsLabel)

        self.field_auto_export_shows = QCheckBox(self.groupBox_4)
        self.field_auto_export_shows.setObjectName(u"field_auto_export_shows")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.field_auto_export_shows)

        self.autoExportCalendarsLabel = QLabel(self.groupBox_4)
        self.autoExportCalendarsLabel.setObjectName(u"autoExportCalendarsLabel")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.autoExportCalendarsLabel)

        self.field_auto_export_calendars = QCheckBox(self.groupBox_4)
        self.field_auto_export_calendars.setObjectName(u"field_auto_export_calendars")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.field_auto_export_calendars)


        self.verticalLayout_6.addLayout(self.formLayout_3)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.paths_exports, "")
        self.customlinks = QWidget()
        self.customlinks.setObjectName(u"customlinks")
        self.verticalLayout_2 = QVBoxLayout(self.customlinks)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_custom_links = QTableWidget(self.customlinks)
        if (self.table_custom_links.columnCount() < 2):
            self.table_custom_links.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_custom_links.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_custom_links.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_custom_links.setObjectName(u"table_custom_links")
        self.table_custom_links.setProperty(u"showDropIndicator", True)
        self.table_custom_links.setDragEnabled(True)
        self.table_custom_links.setDragDropOverwriteMode(True)
        self.table_custom_links.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.table_custom_links.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.table_custom_links.setAlternatingRowColors(False)
        self.table_custom_links.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_custom_links.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_custom_links.setCornerButtonEnabled(True)
        self.table_custom_links.horizontalHeader().setCascadingSectionResizes(True)
        self.table_custom_links.horizontalHeader().setDefaultSectionSize(200)
        self.table_custom_links.horizontalHeader().setStretchLastSection(True)
        self.table_custom_links.verticalHeader().setVisible(False)
        self.table_custom_links.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_2.addWidget(self.table_custom_links)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_insert_link = QPushButton(self.customlinks)
        self.bt_insert_link.setObjectName(u"bt_insert_link")

        self.horizontalLayout_2.addWidget(self.bt_insert_link)

        self.bt_insert_separator = QPushButton(self.customlinks)
        self.bt_insert_separator.setObjectName(u"bt_insert_separator")

        self.horizontalLayout_2.addWidget(self.bt_insert_separator)

        self.bt_delete_link = QPushButton(self.customlinks)
        self.bt_delete_link.setObjectName(u"bt_delete_link")

        self.horizontalLayout_2.addWidget(self.bt_delete_link)

        self.bt_test = QPushButton(self.customlinks)
        self.bt_test.setObjectName(u"bt_test")

        self.horizontalLayout_2.addWidget(self.bt_test)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.customlinks, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Defaults", None))
        self.homebaseCityLabel.setText(QCoreApplication.translate("SettingsDialog", u"Homebase City", None))
#if QT_CONFIG(tooltip)
        self.field_homebase_city.setToolTip(QCoreApplication.translate("SettingsDialog", u"Name of your homebase's city", None))
#endif // QT_CONFIG(tooltip)
        self.geocoordinatesLabel.setText(QCoreApplication.translate("SettingsDialog", u"Geo-Coordinates (Lat, Lon)", None))
#if QT_CONFIG(tooltip)
        self.field_geocoordinates.setToolTip(QCoreApplication.translate("SettingsDialog", u"The homebase's position (decimal), e.g. 47.994853, 7.843950", None))
#endif // QT_CONFIG(tooltip)
        self.artistLabel.setText(QCoreApplication.translate("SettingsDialog", u"Artist", None))
#if QT_CONFIG(tooltip)
        self.field_artist.setToolTip(QCoreApplication.translate("SettingsDialog", u"Default artist name", None))
#endif // QT_CONFIG(tooltip)
        self.currencyLabel.setText(QCoreApplication.translate("SettingsDialog", u"Currency", None))
#if QT_CONFIG(tooltip)
        self.field_currency.setToolTip(QCoreApplication.translate("SettingsDialog", u"Default currency e.g. EUR, \u20ac, USD, $", None))
#endif // QT_CONFIG(tooltip)
        self.distanceUnitLabel.setText(QCoreApplication.translate("SettingsDialog", u"Distance Unit", None))
#if QT_CONFIG(tooltip)
        self.field_distance_unit.setToolTip(QCoreApplication.translate("SettingsDialog", u"Default distance unit, e.g. km, miles", None))
#endif // QT_CONFIG(tooltip)
        self.travelUnitPriceLabel.setText(QCoreApplication.translate("SettingsDialog", u"Travel Unit Price", None))
#if QT_CONFIG(tooltip)
        self.field_travel_unit_price.setToolTip(QCoreApplication.translate("SettingsDialog", u"Default price per distance unit, e.g. 0,3 \u20ac / km", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsDialog", u"View", None))
#if QT_CONFIG(tooltip)
        self.themeLabel.setToolTip(QCoreApplication.translate("SettingsDialog", u"* Needs application restart", None))
#endif // QT_CONFIG(tooltip)
        self.themeLabel.setText(QCoreApplication.translate("SettingsDialog", u"Theme*", None))
#if QT_CONFIG(tooltip)
        self.field_theme.setToolTip(QCoreApplication.translate("SettingsDialog", u"Set the interface's appearance.\n"
"Needs an application restart.", None))
#endif // QT_CONFIG(tooltip)
        self.fontSizeLabel.setText(QCoreApplication.translate("SettingsDialog", u"Font Size", None))
#if QT_CONFIG(tooltip)
        self.field_fontsize.setToolTip(QCoreApplication.translate("SettingsDialog", u"Font size", None))
#endif // QT_CONFIG(tooltip)
        self.fieldAreaWidthLabel.setText(QCoreApplication.translate("SettingsDialog", u"Field Area Width (px)", None))
#if QT_CONFIG(tooltip)
        self.field_field_area_width.setToolTip(QCoreApplication.translate("SettingsDialog", u"The width of the field areas (left and right of the main window)", None))
#endif // QT_CONFIG(tooltip)
        self.saveAndRestoreWindowSizeLabel.setText(QCoreApplication.translate("SettingsDialog", u"Save and Restore Window Size", None))
#if QT_CONFIG(tooltip)
        self.field_save_window_size.setToolTip(QCoreApplication.translate("SettingsDialog", u"Save and restore window size", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Start with Selected Show", None))
#if QT_CONFIG(tooltip)
        self.field_start_with_selected_show.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select previously selected show on start", None))
#endif // QT_CONFIG(tooltip)
        self.calculatorTextDecimalSeparatorLabel.setText(QCoreApplication.translate("SettingsDialog", u"Calculator Text Decimal Separator", None))
#if QT_CONFIG(tooltip)
        self.field_calc_text_decimal_separator.setToolTip(QCoreApplication.translate("SettingsDialog", u"Set decimal separator in the Travel Costs Calculator's auto generated text", None))
#endif // QT_CONFIG(tooltip)
        self.mapProviderLabel.setText(QCoreApplication.translate("SettingsDialog", u"Map Provider", None))
#if QT_CONFIG(tooltip)
        self.field_map_provider.setToolTip(QCoreApplication.translate("SettingsDialog", u"Map provider (osm or gmaps)", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.defaults), QCoreApplication.translate("SettingsDialog", u"Defaults and View", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SettingsDialog", u"Paths", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("SettingsDialog", u"* Needs application restart", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Working Folder*", None))
#if QT_CONFIG(tooltip)
        self.field_workdir.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.field_workdir.setStatusTip(QCoreApplication.translate("SettingsDialog", u"The path to the working folder (containing the databases)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.bt_select_workdir.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select a folder manually", None))
#endif // QT_CONFIG(tooltip)
        self.bt_select_workdir.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
        self.label_6.setText(QCoreApplication.translate("SettingsDialog", u"~", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Show Calendar", None))
#if QT_CONFIG(tooltip)
        self.field_show_calendar_path.setToolTip(QCoreApplication.translate("SettingsDialog", u"TourManagerShows.ics:\n"
"A calendar file containing the shows", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.field_show_calendar_path.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.bt_copy_show_calendar.setToolTip(QCoreApplication.translate("SettingsDialog", u"Copy path to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.bt_copy_show_calendar.setText(QCoreApplication.translate("SettingsDialog", u"Copy", None))
#if QT_CONFIG(tooltip)
        self.bt_copy_event_calendar.setToolTip(QCoreApplication.translate("SettingsDialog", u"Copy path to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.bt_copy_event_calendar.setText(QCoreApplication.translate("SettingsDialog", u"Copy", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Event Calendar", None))
#if QT_CONFIG(tooltip)
        self.field_event_calendar_path.setToolTip(QCoreApplication.translate("SettingsDialog", u"TourManagerEvents.ics:\n"
"A calendar file containing the events", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.field_event_calendar_path.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"Event Forecast Calendar", None))
#if QT_CONFIG(tooltip)
        self.field_event_forecast_calendar_path.setToolTip(QCoreApplication.translate("SettingsDialog", u"TourManagerEventsForecast.ics:\n"
"A calendar file containing the events, but postponed one year ahead", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.field_event_forecast_calendar_path.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.bt_copy_event_forecast_calendar.setToolTip(QCoreApplication.translate("SettingsDialog", u"Copy path to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.bt_copy_event_forecast_calendar.setText(QCoreApplication.translate("SettingsDialog", u"Copy", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SettingsDialog", u"Exports", None))
        self.autoExportFutureShowsLabel.setText(QCoreApplication.translate("SettingsDialog", u"Auto Export Future Shows", None))
#if QT_CONFIG(tooltip)
        self.field_auto_export_shows.setToolTip(QCoreApplication.translate("SettingsDialog", u"Exports: FutureShows.html (Upcoming and Work in Progress Shows)", None))
#endif // QT_CONFIG(tooltip)
        self.autoExportCalendarsLabel.setText(QCoreApplication.translate("SettingsDialog", u"Auto Export Calendars", None))
#if QT_CONFIG(tooltip)
        self.field_auto_export_calendars.setToolTip(QCoreApplication.translate("SettingsDialog", u"Exports:\n"
"TourManagerShows.ics\n"
"TourManagerEvents.ics\n"
"TourManagerEventsForecast.ics", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.paths_exports), QCoreApplication.translate("SettingsDialog", u"Paths and Exports", None))
        ___qtablewidgetitem = self.table_custom_links.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SettingsDialog", u"Name", None));
        ___qtablewidgetitem1 = self.table_custom_links.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SettingsDialog", u"Path", None));
#if QT_CONFIG(tooltip)
        self.bt_insert_link.setToolTip(QCoreApplication.translate("SettingsDialog", u"Insert blank line after selected link", None))
#endif // QT_CONFIG(tooltip)
        self.bt_insert_link.setText(QCoreApplication.translate("SettingsDialog", u"Insert Blank Link", None))
#if QT_CONFIG(tooltip)
        self.bt_insert_separator.setToolTip(QCoreApplication.translate("SettingsDialog", u"Insert separator after selected link", None))
#endif // QT_CONFIG(tooltip)
        self.bt_insert_separator.setText(QCoreApplication.translate("SettingsDialog", u"Insert Separator", None))
#if QT_CONFIG(tooltip)
        self.bt_delete_link.setToolTip(QCoreApplication.translate("SettingsDialog", u"Delete selected link", None))
#endif // QT_CONFIG(tooltip)
        self.bt_delete_link.setText(QCoreApplication.translate("SettingsDialog", u"Delete Link", None))
        self.bt_test.setText(QCoreApplication.translate("SettingsDialog", u"test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customlinks), QCoreApplication.translate("SettingsDialog", u"Custom Links", None))
    # retranslateUi


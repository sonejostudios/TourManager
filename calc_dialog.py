# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_CalcDialog(object):
    def setupUi(self, CalcDialog):
        if not CalcDialog.objectName():
            CalcDialog.setObjectName(u"CalcDialog")
        CalcDialog.resize(338, 104)
        self.verticalLayout = QVBoxLayout(CalcDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.spinbox_travel_distance = QSpinBox(CalcDialog)
        self.spinbox_travel_distance.setObjectName(u"spinbox_travel_distance")
        self.spinbox_travel_distance.setMinimumSize(QSize(60, 0))
        self.spinbox_travel_distance.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spinbox_travel_distance.setMaximum(999999)
        self.spinbox_travel_distance.setSingleStep(1)

        self.horizontalLayout_11.addWidget(self.spinbox_travel_distance)

        self.label_distance_unit = QLabel(CalcDialog)
        self.label_distance_unit.setObjectName(u"label_distance_unit")

        self.horizontalLayout_11.addWidget(self.label_distance_unit)

        self.cb_travel_distance_2x = QCheckBox(CalcDialog)
        self.cb_travel_distance_2x.setObjectName(u"cb_travel_distance_2x")
        self.cb_travel_distance_2x.setChecked(True)

        self.horizontalLayout_11.addWidget(self.cb_travel_distance_2x)

        self.label_36 = QLabel(CalcDialog)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_36)

        self.spinbox_travel_price = QDoubleSpinBox(CalcDialog)
        self.spinbox_travel_price.setObjectName(u"spinbox_travel_price")
        self.spinbox_travel_price.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinbox_travel_price.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spinbox_travel_price.setSingleStep(0.010000000000000)
        self.spinbox_travel_price.setValue(0.300000000000000)

        self.horizontalLayout_11.addWidget(self.spinbox_travel_price)

        self.label_37 = QLabel(CalcDialog)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_37)

        self.spinbox_result = QDoubleSpinBox(CalcDialog)
        self.spinbox_result.setObjectName(u"spinbox_result")
        self.spinbox_result.setMinimumSize(QSize(80, 0))
        self.spinbox_result.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinbox_result.setInputMethodHints(Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.spinbox_result.setReadOnly(True)
        self.spinbox_result.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox_result.setMaximum(999999.989999999990687)

        self.horizontalLayout_11.addWidget(self.spinbox_result)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.travel_costs_text_label = QLabel(CalcDialog)
        self.travel_costs_text_label.setObjectName(u"travel_costs_text_label")

        self.horizontalLayout_2.addWidget(self.travel_costs_text_label)

        self.bt_copy_text = QPushButton(CalcDialog)
        self.bt_copy_text.setObjectName(u"bt_copy_text")
        self.bt_copy_text.setMaximumSize(QSize(40, 16777215))
        self.bt_copy_text.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.bt_copy_text)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(CalcDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close|QDialogButtonBox.StandardButton.Reset)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CalcDialog)
        self.buttonBox.accepted.connect(CalcDialog.accept)
        self.buttonBox.rejected.connect(CalcDialog.reject)

        QMetaObject.connectSlotsByName(CalcDialog)
    # setupUi

    def retranslateUi(self, CalcDialog):
        CalcDialog.setWindowTitle(QCoreApplication.translate("CalcDialog", u"Calc", None))
        self.label_distance_unit.setText(QCoreApplication.translate("CalcDialog", u"Unit", None))
#if QT_CONFIG(tooltip)
        self.cb_travel_distance_2x.setToolTip(QCoreApplication.translate("CalcDialog", u"Back and forth", None))
#endif // QT_CONFIG(tooltip)
        self.cb_travel_distance_2x.setText(QCoreApplication.translate("CalcDialog", u"* 2", None))
        self.label_36.setText(QCoreApplication.translate("CalcDialog", u"*", None))
#if QT_CONFIG(tooltip)
        self.spinbox_travel_price.setToolTip(QCoreApplication.translate("CalcDialog", u"Price per Distance Unit", None))
#endif // QT_CONFIG(tooltip)
        self.spinbox_travel_price.setSuffix("")
        self.label_37.setText(QCoreApplication.translate("CalcDialog", u"=", None))
#if QT_CONFIG(tooltip)
        self.spinbox_result.setToolTip(QCoreApplication.translate("CalcDialog", u"Travel costs", None))
#endif // QT_CONFIG(tooltip)
        self.travel_costs_text_label.setText(QCoreApplication.translate("CalcDialog", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.bt_copy_text.setToolTip(QCoreApplication.translate("CalcDialog", u"Copy travel costs text to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.bt_copy_text.setText(QCoreApplication.translate("CalcDialog", u"Copy", None))
    # retranslateUi


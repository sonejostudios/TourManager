# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_show_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_AddShowDialog(object):
    def setupUi(self, AddShowDialog):
        if not AddShowDialog.objectName():
            AddShowDialog.setObjectName(u"AddShowDialog")
        AddShowDialog.resize(241, 94)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddShowDialog.sizePolicy().hasHeightForWidth())
        AddShowDialog.setSizePolicy(sizePolicy)
        AddShowDialog.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(AddShowDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(AddShowDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.dateEdit = QDateEdit(AddShowDialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEdit)

        self.label_2 = QLabel(AddShowDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lb_venue_name = QLabel(AddShowDialog)
        self.lb_venue_name.setObjectName(u"lb_venue_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lb_venue_name)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(AddShowDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddShowDialog)
        self.buttonBox.accepted.connect(AddShowDialog.accept)
        self.buttonBox.rejected.connect(AddShowDialog.reject)

        QMetaObject.connectSlotsByName(AddShowDialog)
    # setupUi

    def retranslateUi(self, AddShowDialog):
        AddShowDialog.setWindowTitle(QCoreApplication.translate("AddShowDialog", u"Add New Show", None))
        self.label.setText(QCoreApplication.translate("AddShowDialog", u"Show Date", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("AddShowDialog", u"yyyy-MM-dd", None))
        self.label_2.setText(QCoreApplication.translate("AddShowDialog", u"Venue", None))
        self.lb_venue_name.setText(QCoreApplication.translate("AddShowDialog", u"None", None))
    # retranslateUi


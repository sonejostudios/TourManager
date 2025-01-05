# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_venue_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_AddVenueDialog(object):
    def setupUi(self, AddVenueDialog):
        if not AddVenueDialog.objectName():
            AddVenueDialog.setObjectName(u"AddVenueDialog")
        AddVenueDialog.resize(240, 128)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddVenueDialog.sizePolicy().hasHeightForWidth())
        AddVenueDialog.setSizePolicy(sizePolicy)
        AddVenueDialog.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(AddVenueDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(AddVenueDialog)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.field_venue_name = QLineEdit(AddVenueDialog)
        self.field_venue_name.setObjectName(u"field_venue_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.field_venue_name)

        self.cityLabel = QLabel(AddVenueDialog)
        self.cityLabel.setObjectName(u"cityLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cityLabel)

        self.field_venue_city = QLineEdit(AddVenueDialog)
        self.field_venue_city.setObjectName(u"field_venue_city")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.field_venue_city)

        self.countryLabel = QLabel(AddVenueDialog)
        self.countryLabel.setObjectName(u"countryLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.countryLabel)

        self.field_venue_country = QLineEdit(AddVenueDialog)
        self.field_venue_country.setObjectName(u"field_venue_country")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.field_venue_country)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(AddVenueDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddVenueDialog)
        self.buttonBox.accepted.connect(AddVenueDialog.accept)
        self.buttonBox.rejected.connect(AddVenueDialog.reject)

        QMetaObject.connectSlotsByName(AddVenueDialog)
    # setupUi

    def retranslateUi(self, AddVenueDialog):
        AddVenueDialog.setWindowTitle(QCoreApplication.translate("AddVenueDialog", u"Add New Venue", None))
        self.nameLabel.setText(QCoreApplication.translate("AddVenueDialog", u"Name", None))
        self.cityLabel.setText(QCoreApplication.translate("AddVenueDialog", u"City", None))
        self.countryLabel.setText(QCoreApplication.translate("AddVenueDialog", u"Country", None))
    # retranslateUi


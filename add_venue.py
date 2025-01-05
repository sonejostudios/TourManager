from PySide6.QtWidgets import QDialog, QDialogButtonBox


# import mainwindow.py as module and it's main class
from add_venue_dialog import Ui_AddVenueDialog




class AddVenueDialog(QDialog):
    def __init__(self, parent, city, country):
        super(AddVenueDialog, self).__init__(parent)
        self.ui_dialog = Ui_AddVenueDialog()
        self.ui_dialog.setupUi(self)
        self.setWindowTitle("New Venue")
        self.setFixedSize(self.size())

        # fill city and country fields
        self.ui_dialog.field_venue_city.setText(city)
        self.ui_dialog.field_venue_country.setText(country)


        # disable ok button
        self.ui_dialog.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)


        #signals
        self.ui_dialog.field_venue_name.textChanged.connect(self.check_fields)
        self.ui_dialog.field_venue_city.textChanged.connect(self.check_fields)
        self.ui_dialog.field_venue_country.textChanged.connect(self.check_fields)





    def on_ok(self):
        name = self.ui_dialog.field_venue_name.text()
        city = self.ui_dialog.field_venue_city.text()
        country = self.ui_dialog.field_venue_country.text()
        return name, city, country


    def check_fields(self): # and set ok button state
        if self.ui_dialog.field_venue_name.text() == "" or self.ui_dialog.field_venue_city.text() == "" or self.ui_dialog.field_venue_country.text() == "":
            self.ui_dialog.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui_dialog.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

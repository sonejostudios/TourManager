from PySide6.QtWidgets import QDialog, QDialogButtonBox

# import mainwindow.py as module and it's main class
from add_venue_dialog import Ui_AddVenueDialog




class AddVenueDialog(QDialog):
    def __init__(self, parent, city, country):
        super(AddVenueDialog, self).__init__(parent)
        self.ui_dialog = Ui_AddVenueDialog()
        self.ui_dialog.setupUi(self)
        self.setWindowTitle("Create New Venue/Event")
        self.setFixedSize(self.size())

        # fill city and country fields
        #self.ui_dialog.field_venue_city.setText(city)
        #self.ui_dialog.field_venue_country.setText(country)

        self.ui_dialog.field_venue_city.clear()
        self.ui_dialog.field_venue_city.addItems(sorted(set(parent.df_venues['VenueCity'].tolist()), key=str.casefold))
        self.ui_dialog.field_venue_city.setCurrentText(city)

        # country cb
        self.ui_dialog.field_venue_country.clear()
        self.ui_dialog.field_venue_country.addItems(sorted(set(parent.df_venues['VenueCountry'].tolist()), key=str.casefold))
        self.ui_dialog.field_venue_country.setCurrentText(country)


        # disable ok button
        self.ui_dialog.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)


        #signals
        self.ui_dialog.field_venue_name.textChanged.connect(self.check_fields)
        self.ui_dialog.field_venue_city.currentTextChanged.connect(self.check_fields)
        self.ui_dialog.field_venue_country.currentTextChanged.connect(self.check_fields)



    def check_fields(self): # and set ok button state
        if self.ui_dialog.field_venue_name.text() == "" or self.ui_dialog.field_venue_city.currentText() == "" or self.ui_dialog.field_venue_country.currentText() == "":
            self.ui_dialog.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui_dialog.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)



    def on_ok(self):
        name = self.ui_dialog.field_venue_name.text()
        city = self.ui_dialog.field_venue_city.currentText()
        country = self.ui_dialog.field_venue_country.currentText()
        new_show = bool(self.ui_dialog.cb_create_new_show.isChecked())
        return name, city, country, new_show





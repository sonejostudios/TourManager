from PySide6.QtWidgets import QDialog, QDialogButtonBox
#from PySide6.QtCore import QDate


# import mainwindow.py as module and it's main class
from calc_dialog import Ui_CalcDialog




class CalcDialog(QDialog):
    def __init__(self, parent):
        super(CalcDialog, self).__init__(parent)
        self.ui = Ui_CalcDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Travel Costs Calculator")
        self.setFixedSize(self.size())

        # get config
        self.config_homebase_city = parent.config_homebase_city
        self.config_currency = parent.config_currency
        self.config_distance_unit = parent.config_distance_unit
        self.config_travel_unit_price = parent.config_travel_unit_price

        # apply config
        self.ui.spinbox_travel_distance.setToolTip("Distance from " + self.config_homebase_city)
        self.ui.label_distance_unit.setText(self.config_distance_unit)
        self.ui.spinbox_travel_price.setValue(self.config_travel_unit_price)
        self.ui.spinbox_travel_price.setToolTip("Price/" + self.config_distance_unit )
        self.ui.spinbox_result.setSuffix(" " + self.config_currency)

        # delete 0 in travel distance field
        self.ui.spinbox_travel_distance.clear()

        # signals
        self.ui.spinbox_travel_distance.valueChanged.connect(self.calculate_travel_costs)
        self.ui.cb_travel_distance_2x.stateChanged.connect(self.calculate_travel_costs)
        self.ui.spinbox_travel_price.valueChanged.connect(self.calculate_travel_costs)
        self.ui.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.reset_travel_distance)




    def calculate_travel_costs(self):
        distance = self.ui.spinbox_travel_distance.value()
        back_and_forth = 2 if self.ui.cb_travel_distance_2x.isChecked() else 1
        price = self.ui.spinbox_travel_price.value()
        result = round(distance * back_and_forth * price, 2)
        self.ui.spinbox_result.setValue(result)



    def reset_travel_distance(self):
        self.ui.spinbox_travel_distance.setValue(0)
        self.ui.spinbox_travel_distance.clear()
        self.ui.spinbox_travel_distance.setFocus()
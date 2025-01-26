import time

from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import QDate
from PySide6.QtGui import QGuiApplication

# import mainwindow.py as module and it's main class
from calc_dialog import Ui_CalcDialog




class CalcDialog(QDialog):
    def __init__(self, parent):
        super(CalcDialog, self).__init__(parent)
        self.ui = Ui_CalcDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Travel Costs Calculator")
        self.setFixedSize(self.size())

        self.parent = parent

        # get config
        self.config_homebase_city = parent.config_homebase_city
        self.config_currency = parent.config_currency
        self.config_distance_unit = parent.config_distance_unit
        self.config_travel_unit_price = parent.config_travel_unit_price
        self.config_calc_dec_sep = parent.config_calc_dec_sep

        # apply config
        self.ui.spinbox_travel_distance.setToolTip("Distance from " + self.config_homebase_city)
        self.ui.label_distance_unit.setText(self.config_distance_unit)
        self.ui.spinbox_travel_price.setValue(self.config_travel_unit_price)
        self.ui.spinbox_travel_price.setToolTip("Price/" + self.config_distance_unit )
        self.ui.spinbox_result.setSuffix(" " + self.config_currency)

        # initial setup
        self.ui.spinbox_travel_distance.clear()
        self.ui.travel_costs_text_label.clear()
        self.ui.bt_copy_text.setEnabled(False)


        # signals
        self.ui.spinbox_travel_distance.valueChanged.connect(self.calculate_travel_costs) #enable this to use mouse wheel
        self.ui.spinbox_travel_distance.lineEdit().textChanged.connect(self.calculate_travel_costs) # use underlying lineEdit to send signal even if spinbox is empty
        self.ui.cb_travel_distance_2x.stateChanged.connect(self.calculate_travel_costs)
        self.ui.spinbox_travel_price.valueChanged.connect(self.calculate_travel_costs)
        self.ui.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.reset_travel_distance)
        self.ui.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.closeEvent)
        self.rejected.connect(self.enable_calc_buttons) # when esc key is pressed
        self.ui.bt_copy_text.clicked.connect(self.copy_text)





    def calculate_travel_costs(self):
        if self.ui.spinbox_travel_distance.text() == "": # empty and reset all
            self.ui.travel_costs_text_label.clear()
            self.ui.spinbox_result.setValue(0)
            self.ui.bt_copy_text.setEnabled(False)

        else: # do the calculation
            distance = self.ui.spinbox_travel_distance.value()
            back_and_forth = 2 if self.ui.cb_travel_distance_2x.isChecked() else 1
            price = self.ui.spinbox_travel_price.value()
            result = round(distance * back_and_forth * price, 2)
            self.ui.spinbox_result.setValue(result)

            # generate text
            text = str(distance * back_and_forth) + " " + self.config_distance_unit + " * " + str(round(price,2)) + " " + self.config_currency + "/" + self.config_distance_unit + " = " + str(result) + " " + self.config_currency
            if self.config_calc_dec_sep not in ["", "."]: # replace decimal separator
                text = text.replace(".", self.config_calc_dec_sep)
            self.ui.travel_costs_text_label.setText(text)

            # enable button
            self.ui.bt_copy_text.setEnabled(True)




    def copy_text(self):
        self.clipboard = QGuiApplication.clipboard()
        self.clipboard.setText(self.ui.travel_costs_text_label.text())
        self.parent.ui.statusbar.showMessage("Travel costs text copied to clipboard!", 3000)



    def reset_travel_distance(self):
        self.ui.spinbox_travel_distance.setValue(0)
        self.ui.spinbox_travel_distance.clear()
        self.ui.spinbox_travel_distance.setFocus()

        self.ui.travel_costs_text_label.clear()



    def closeEvent(self, event):
        self.enable_calc_buttons()


    def enable_calc_buttons(self):
        self.parent.ui.bt_calculator.setEnabled(True)
        self.parent.ui.actionTravel_Costs_Calculator.setEnabled(True)

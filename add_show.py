from PySide6.QtWidgets import QDialog, QDialogButtonBox
#from PySide6.QtCore import QDate


# import mainwindow.py as module and it's main class
from add_show_dialog import Ui_AddShowDialog




class AddShowDialog(QDialog):
    def __init__(self, parent, how, date):
        super(AddShowDialog, self).__init__(parent)
        self.ui_dialog = Ui_AddShowDialog()
        self.ui_dialog.setupUi(self)
        self.setWindowTitle(how + " Show")
        self.setFixedSize(self.size())


        #self.ui_dialog.dateEdit.setDate(QDate.currentDate()) # set today

        self.ui_dialog.dateEdit.setDate(date) # set selected date



    def on_ok(self):
        date = self.ui_dialog.dateEdit.date().toString("yyyy-MM-dd")
        print(date)
        return date



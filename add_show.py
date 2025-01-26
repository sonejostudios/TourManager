from PySide6.QtWidgets import QDialog, QDialogButtonBox, QCalendarWidget
from PySide6.QtCore import QDate, Qt, QLocale


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


        # set calendar widgets with week numbers and monday as first day of week
        self.calendar_show = QCalendarWidget(self)
        self.calendar_show.setFirstDayOfWeek(Qt.Monday)
        self.calendar_show.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
        self.ui_dialog.dateEdit.setCalendarWidget(self.calendar_show)



    def on_ok(self):
        date = self.ui_dialog.dateEdit.date().toString("yyyy-MM-dd")
        print(date)
        return date



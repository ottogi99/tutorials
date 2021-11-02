# Ex. QCalendarWidget.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = QLabel(self)

        self.init_ui()

    def init_ui(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.on_date_clicked)

        date = cal.selectedDate()
        self.lbl.setText(date.toString('yyyy-MM-dd'))

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def on_date_clicked(self, date):
        self.lbl.setText(date.toString('yyyy-MM-dd'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


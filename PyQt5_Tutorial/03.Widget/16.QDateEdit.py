# Ex. QDateEdit.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        lbl = QLabel('QDateEdit')

        dateedit = QDateEdit(self)
        dateedit.setDate(QDate.currentDate())
        dateedit.setMinimumDate(QDate(1900, 1, 1))
        dateedit.setMaximumDate(QDate(2100, 12, 31))
        dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(dateedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


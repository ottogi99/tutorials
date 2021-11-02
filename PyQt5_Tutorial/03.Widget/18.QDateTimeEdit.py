# Ex. QDateTimeEdit.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        lbl = QLabel('QDateTimeEdit')

        datetimeedit = QDateTimeEdit(self)
        datetimeedit.setDateTime(QDateTime.currentDateTime())
        datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(datetimeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


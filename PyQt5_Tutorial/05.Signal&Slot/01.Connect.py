# Ex. 연결하기.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit()

        self.init_ui()

    def init_ui(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


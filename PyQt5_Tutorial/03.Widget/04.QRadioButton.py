# Ex. QRadioButton.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        r_btn1 = QRadioButton('First Button', self)
        r_btn1.move(50, 50)
        r_btn1.setChecked(True)

        r_btn2 = QRadioButton(self)
        r_btn2.move(50, 70)
        r_btn2.setText('Second Button')

        self.setWindowTitle('QRadioButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


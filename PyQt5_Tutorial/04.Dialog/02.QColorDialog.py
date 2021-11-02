# Ex. QColorDialog.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Dialog', self)
        self.frm = QFrame(self)

        self.init_ui()

    def init_ui(self):
        col = QColor(0, 0, 0)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.on_btn_clicked)

        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(130, 35, 100, 100)

        self.setWindowTitle('Input dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_btn_clicked(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


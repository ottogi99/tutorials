# Ex. QLineEdit.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = QLabel(self)
        self.le = QLineEdit(self)
        self.init_ui()

    def init_ui(self):
        self.lbl.move(60, 40)
        self.le.move(60, 100)
        self.le.textChanged[str].connect(self.on_changed)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_changed(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


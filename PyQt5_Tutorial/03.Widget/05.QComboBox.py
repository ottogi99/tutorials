# Ex. QComboBox.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = QLabel('Option1', self)
        self.cb = QComboBox(self)
        self.init_ui()

    def init_ui(self):
        self.lbl.move(50, 150)

        self.cb.addItem('Option1')
        self.cb.addItem('Option2')
        self.cb.addItem('Option3')
        self.cb.addItem('Option4')
        self.cb.move(50, 50)

        # self.cb.activated[str].connect(self.on_activated) # Ths function is deprecated.
        self.cb.activated[int].connect(self.on_activated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_activated(self, index):
        text = self.cb.itemText(index)
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


# Ex. QPushButton.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.on_change_title)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_change_title(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Checked')
        else:
            self.setWindowTitle('UnChecked')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


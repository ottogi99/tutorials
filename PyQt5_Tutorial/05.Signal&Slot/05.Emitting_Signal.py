# Ex. 사용자 정의 시그널.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Communicate(QObject):
    closeApp = pyqtSignal()


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.c = Communicate()

        self.init_ui()

    def init_ui(self):
        self.c.closeApp.connect(self.close)

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, event: QMouseEvent):
        self.c.closeApp.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


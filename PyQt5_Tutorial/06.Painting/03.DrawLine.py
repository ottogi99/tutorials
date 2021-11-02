# Ex. 직선 그리기

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('drawLine')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def paintEvent(self, event: QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()

    def draw_line(self, qp):
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawLine(30, 230, 200, 50)
        qp.setPen(QPen(Qt.green, 12))
        qp.drawLine(140, 60, 320, 280)
        qp.setPen(QPen(Qt.red, 16))
        qp.drawLine(330, 250, 40, 190)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


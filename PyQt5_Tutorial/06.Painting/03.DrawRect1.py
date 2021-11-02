# Ex. 직사각형 그리기

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
        self.setWindowTitle('drawRect')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def paintEvent(self, event: QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(QColor(180, 100, 160))
        qp.setPen(QPen(QColor(60, 60, 60), 8))
        qp.drawRect(20, 20, 100, 100)

        qp.setBrush(QColor(40, 150, 20))
        qp.setPen(QPen(Qt.blue, 2))
        qp.drawRect(180, 120, 50, 120)

        qp.setBrush(Qt.yellow)
        qp.setPen(QPen(Qt.red, 5))
        qp.drawRect(280, 30, 80, 40)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


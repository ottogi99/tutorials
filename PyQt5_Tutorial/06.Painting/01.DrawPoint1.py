# Ex. 점 그리기

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Points')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def paintEvent(self, event: QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawPoint(self.width() / 2, self.height() / 2)
        qp.setPen(QPen(Qt.green, 12))
        qp.drawPoint(self.width() / 4, 3 * self.height() / 4)
        qp.setPen(QPen(Qt.red, 16))
        qp.drawPoint(3 * self.width() / 4, self.height() / 4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


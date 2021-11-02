# Ex. QSplitter.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        h_box = QHBoxLayout()

        top = QFrame()
        top.setFrameShape(QFrame.Box)

        mid_left = QFrame()
        mid_left.setFrameShape(QFrame.StyledPanel)

        mid_right = QFrame()
        mid_right.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(mid_left)
        splitter1.addWidget(mid_right)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        h_box.addWidget(splitter2)
        self.setLayout(h_box)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def on_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


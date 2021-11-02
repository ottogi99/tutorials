# Ex. QFontDialog.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = QLabel('The quick brown fox jumps ove the lazy dog', self)

        self.init_ui()

    def init_ui(self):
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        btn.clicked.connect(self.on_btn_clicked)

        self.lbl.move(130, 20)

        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('Font dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_btn_clicked(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


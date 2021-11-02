# Ex. QTextEdit.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.lbl2 = QLabel('The number of words is 0')

        self.init_ui()

    def init_ui(self):
        self.te.setAcceptRichText(False)
        self.te.textChanged.connect(self.on_text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The numb of words is ' + str(len(text.split())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


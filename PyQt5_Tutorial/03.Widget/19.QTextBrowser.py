# Ex. QDateTimeEdit.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.le = QLineEdit()
        self.tb = QTextBrowser()
        self.clear_btn = QPushButton('Clear')

        self.init_ui()

    def init_ui(self):
        self.le.returnPressed.connect(self.append_text)
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.clear_btn.pressed.connect(self.clear_text)

        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        self.tb.clear()

# -- 입력창에 아래와 같은 형식으로 입력 --
# Plain Text
# <b>Bold</b>
# <i>Italic</i>
# <p style="color: red">Red</p>
# <p style="font-size: 20px">20px</p>
# <a href="https://www.naver.com">Naver</a>


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


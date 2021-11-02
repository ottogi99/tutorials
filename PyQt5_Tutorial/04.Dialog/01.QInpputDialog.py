# Ex. QInputDialog.

import sys

from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Dialog', self)
        self.le = QLineEdit(self)

        self.init_ui()

    def init_ui(self):
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.on_btn_clicked)

        self.le.move(120, 35)

        self.setWindowTitle('Input dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_btn_clicked(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name: ')

        if ok:
            self.le.setText(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


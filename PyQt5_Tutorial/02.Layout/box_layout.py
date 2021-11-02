# Ex. 박스 레이아웃

import sys

from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_button = QPushButton('OK')
        cancel_button = QPushButton('Cancel')

        h_box = QHBoxLayout()
        h_box.addStretch(1)     # 신축성 있는 빈공간을 제공
        h_box.addWidget(ok_button)
        # h_box.addStretch(1)
        h_box.addWidget(cancel_button)
        h_box.addStretch(1)

        v_box = QVBoxLayout()
        v_box.addStretch(3)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle('Box 02.Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


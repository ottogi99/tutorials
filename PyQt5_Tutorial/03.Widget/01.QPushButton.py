# Ex. QPushButton.

import sys

from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn1 = QPushButton('&Button1', self)    # 단축키 'Alt+B'
        btn1.setCheckable(True)     # 선택되거나 선택되지 않은 상태를 유지
        btn1.toggle()               # 버튼의 상태가 바뀌게 됩니다.

        btn2 = QPushButton(self)
        btn2.setText('Button&2')    # 단축키 'Alt+2'

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        v_box = QVBoxLayout()
        v_box.addWidget(btn1)
        v_box.addWidget(btn2)
        v_box.addWidget(btn3)

        self.setLayout(v_box)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


## Ex. 창 닫기.


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        # PyQt5 에서의 이벤트 처리는 시그널과 슬롯 메커니즘으로 이루어집니다.
        # 버튼(btn)을 클릭하면 'clicked' 시그널이 만들어집니다.
        # instance()
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())

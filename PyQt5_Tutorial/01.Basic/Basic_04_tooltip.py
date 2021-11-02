## Ex. 툴팁 나타내기


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        # sizeHint() 메서드는 버튼을 적절한 크기로 설정하도록 도와줍니다.
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())

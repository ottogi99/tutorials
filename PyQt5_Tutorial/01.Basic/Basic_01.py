## Ex. 창 띄우기.

import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)    # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    ex = MyApp()
    sys.exit(app.exec())

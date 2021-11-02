## Ex. 창 띄우기.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('../../pyqt/asset/web.png'))
        # Geometry: 삼차원의 공간에 있는 물체를 표현하는 점들과 파라미터
        # 창의 위치와 크기를 설정 (x, y, w, h)
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)    # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    ex = MyApp()
    sys.exit(app.exec())

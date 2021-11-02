## Ex. 상태바 만들기
# 메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의 레이아웃을 가지고 있습니다.
# 또한 가운데 영역에 중심위젯(Central widget)을 위한 영역을 갖고 있습니다. 여기에는 어떠한 위젯도 들어올 수 있습니다.


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('../../pyqt/asset/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # Alt+F 를 메뉴의 단축키로 설정
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('StatusBar & Menubar & ToolBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())

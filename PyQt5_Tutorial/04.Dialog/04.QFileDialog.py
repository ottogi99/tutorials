# Ex. QFileDialog.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit()

        self.init_ui()

    def init_ui(self):
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('../asset/open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.show_dialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setWindowTitle('File dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def show_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/')

        if fname[0]:
            f = open(fname[0], 'r', encoding='UTF8')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


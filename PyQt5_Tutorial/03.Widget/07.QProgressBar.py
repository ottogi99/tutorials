# Ex. QProgressBar.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.progressbar = QProgressBar(self)
        self.button = QPushButton('Start', self)
        self.timer = QBasicTimer()
        self.step = 0
        self.init_ui()

    def init_ui(self):
        self.progressbar.setGeometry(30, 40, 200, 25)
        self.button.move(40, 80)
        self.button.clicked.connect(self.on_clicked)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_clicked(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)
            self.button.setText('Stop')

    # QBasicTimer()에 의해 호출되는 핸들러
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.button.setText('Finished')
            return

        self.step += 1
        self.progressbar.setValue(self.step)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


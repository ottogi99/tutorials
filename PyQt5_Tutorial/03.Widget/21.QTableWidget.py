# Ex. QTableWidget.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget()

        self.init_ui()

    def init_ui(self):
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)               # 헤더의 폭이 위젯의 폭에 맞춰지도록 합니다.
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)    # 헤더의 폭이 항목 값의 폭에 맞춰지도록 합니다.

        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(i+j)))

        vbox = QVBoxLayout()
        vbox.addWidget(self.tableWidget)

        self.setLayout(vbox)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


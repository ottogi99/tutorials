# 예제 내용
# * QListView 기본 사용법
# * QStandardItemModel 과 QStandardItem 이용

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *

__company__ = "ONTHESYS"


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ItemView QListView")
        self.setFixedHeight(100)

        fruits = ["banana", "apple", "melon", "pear"]

        view = QListView(self)
        model = QStandardItemModel()
        for f in fruits:
            model.appendRow(QStandardItem(f))
        view.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exit(app.exec())

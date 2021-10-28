# 예제 내용
# * QListView 기본 사용법
# * QAbstractListModel 을 이용한 사용자 모델 생성

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

__company__ = "ONTHESYS"


class UserModel(QAbstractListModel):
    # 2차원 배열을 사용한 사용자 정의 모델 생성자 : 2차원 리스트 초기화 방법
    def __init__(self, rows, columns):
        self._list = [[0 for col in range(columns)] for row in range(rows)]

    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._data)

    # QModelIndex
    # QModelIndex.child(row, column)
    # QModelIndex.column()
    # QModelIndex.row()
    # QModelIndex.data([role=Qt.DisplayRole])
    # QModelIndex.parent()
    # QModelIndex.sibling(row, column)

    # QtCore.QAbstractItemModel.data(index[, role=Qt.DisplayRole])
    def data(self, QModelIndex, role=None):
        item = self._data[QModelIndex.row()]
        # print(QModelIndex.row(), QModelIndex.column())

        if role == Qt.DisplayRole:
            return "%s" % (item['name'])
        elif role == Qt.DecorationRole:
            return QColor(item['color'])
        elif role == Qt.BackgroundRole:
            # return QBrush(Qt.Dense7Pattern)
            # return QBrush(Qt.yellow)
            return QBrush(QColor(item['bg_color']))
        elif role == Qt.ToolTipRole:
            return "Tool Tip: %s" % (item['name'])
        return QVariant()


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ItemView QListView")
        self.setFixedWidth(210)
        self.setFixedHeight(100)

        fruits = [
            # 아이템을 딕셔너리로 구성
            {"name": "banana", "color": "yellow", "bg_color": "yellow"},
            {"name": "apple", "color": "red", "bg_color": "red"},
            {"name": "pear", "color": "green", "bg_color": "gray"},
        ]

        view = QListView(self)
        model = UserModel(fruits)
        view.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exit(app.exec())

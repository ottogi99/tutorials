# QStandardItemModel은 표준 Qt 데이터 유형의 저장소로 사용할 수 있습니다.
# It is one of the Model/View Classes and is part of Qt's model/view framework.

# QStandardItemModel은 모델 작업에 대한 고전적인 항목 기반 접근 방식을 제공합니다.
# The items in a QStandardItemModel are provided by QStandardItem.

# QStandardItemModel은 QAbstractItemModel 인터페이스를 구현합니다.
# which means that the model can be used to provide data in any view that supports that interface
# (such as QListView, QTableView and QTreeView, and your own custom views).
# 성능과 유연성을 위해 QAbstractItemModel을 하위 클래스화하여 다양한 종류의 데이터 저장소에 대한 지원을 제공할 수 있습니다.
# For example, the QDirModel provides a model interface to the underlying file system.

# 목록이나 트리를 원할 때 일반적으로 빈 QStandardItemModel을 만들고 appendRow()를 사용하여
# 모델에 항목을 추가하고 item()을 사용하여 항목에 엑세스합니다.
# If your model represents a table, you typically pass the dimensions of the table to the QStandardItemModel constructor
# and use setItem() to position items into the table.
# setRowCount() 및 setColumnCount()를 사용하여 모델의 차원을 변경할 수도 있습니다.
# To insert items, use insertRow() or insertColumn(), and to remove items,
# use removeRow() or removeColumn().

# setHorizontalHeaderLabels() 및 setVerticalHeaderLabels()를 사용하여 모델의 헤더 레이블을 설정할 수 있습니다.

# You can search for items in the model with findItems(), and sort the model by calling sort().

# 모델에서 모든 항목을 제거하려면 clear()를 호출합니다.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class App(QWidget):
    def __init__(self):
        super().__init__()

        # An Example usage of QStandardItemModel to create table:
        model = QStandardItemModel(4, 4)
        for row in range(4):
            for column in range(4):
                item = QStandardItem("row %d, column %d" % (row, column))
                model.setItem(row, column, item)

        # An example usage of QStandardItemModel to create a tree
        model = QStandardItemModel()
        parentItem = model.invisibleRootItem()
        for i in range(4):
            item = QStandardItem("item %d" % i)
            parentItem.appendRow(item)
            parentItem = item

        treeView = QTreeView(self)
        treeView.setModel(model)
        treeView.clicked[QModelIndex].connect(self.clicked)




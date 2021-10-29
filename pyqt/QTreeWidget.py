# --- Detailed Description
# QTreeWidget 클래스는 Qt3의 QListView 클래스에서 사용하는 것과 유사한 클래스 항목 기반 인터페이스가 있는 표준 트리 위젯을 제공하는 편리한
# 클래스입니다. This class is based on Qt's Model/View architecture and uses a default model to hold items, each of which
# is a QTreeWidgetItem.

# Model/View 프레임워크의 유연성이 필요하지 않은 개발자는 이 클래스를 사용하여 간단한 계층적 목록을 쉽게 만들 수 있습니다. A more flexible
# approach involves combining a QTreeViw with a standard item model. (보다 유연한 접근 방식은 QTreeView를 표준 항목 모델과 결합
# 하는 것입니다. This allows the storage of data to be separated from its representation. (이렇게 하면 데이터의 저장이 해당
# 표현과 분리될 수 있습니다.)

# 가장 간단한 형태의 트리 위젯은 다음과 같은 방식으로 구성할 수 있습니다.
# treeWidget = QTreeWidget()
# treeWidget.setColumnCount(1)
# items = []
# for i in range(10):
#   items.append(QTreeWidgetItem(None, QStringList(QString("item: %1").arg(i)))
# treeWidget.insertTopLevelItems(None, items)
# 항목을 트리위젯에 추가하려면 먼저 setColumnCount() 사용하여 열 수를 설정해야 합니다. This allows each item to have one or more
# labels or other decorations. 사용 중인 열의 수는 columnCount() 함수로 확인할 수 있습니다.

# The tree can have a header that contains a section for each column in the widget. setHeaderLabel() 로 문자열 목록을
# 제공하며 각 섹션에 대한 레이블을 설정하는 것이 가장 쉽지만 사용자 정의 헤더는 QTreeWidgetItem으로고 구성하 setHeaderItem() 함수를
# 사용하여 트리에 삽입할 수 있습니다.

# The items in the tree can be sorted by column according to a predefined sort order. 정렬이 활성화된 경우 사용자는 열
# 머리글을 클릭하여 항목을 정렬할 수 있습니다. Sorting can be enabled or disabled by calling setSortingEnabled().
# isSortingEnabled() 함수는 정렬이 활성화되었는지 여부를 나타냅니다.


import sys

from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle('Test Signal')

        # QTreeView 추가
        head_item = QTreeWidgetItem()
        head_item.setText(0, "Header1")
        head_item.setText(1, "Header2")

        self.root_tree = QTreeWidget()
        self.root_tree.setHeaderItem(head_item)
        self.root_tree.header().setVisible(True)
        self.root_tree.setAlternatingRowColors(True)
        self.root_tree.itemCollapsed.connect(self.collapsed_event)
        self.root_tree.itemExpanded.connect(self.expanded_event)

        item1 = QTreeWidgetItem(self.root_tree)
        item1.setText(0, "A1")

        item2 = QTreeWidgetItem(self.root_tree)
        item2.setText(0, "B1")

        sub_item1 = QTreeWidgetItem(item1)
        sub_item1.setText(0, "A11")

        sub_item2 = QTreeWidgetItem(item2)
        sub_item2.setText(0, "B11")

        # 제일 상위 트리에 추가하기
        item3 = QTreeWidgetItem()
        item3.setText(0, "C1")
        self.root_tree.insertTopLevelItem(0, item3)

        # 화면 전체에 추가
        self.setCentralWidget(self.root_tree)

    def collapsed_event(self, item):
        print('collapsed_event: ', item.text(0))

    def expanded_event(self, item):
        print('expanded_event: ', item.text(0))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

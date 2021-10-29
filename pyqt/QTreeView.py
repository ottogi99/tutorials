# --- Detailed Description
# QTreeView는 모델에서 항목의 트리 표현을 구현합니다. This class is used to provide standard hierarchical lists that were
# previously provided by the QListView class, but using the more flexible approach provided by Qt's model/view
# architecture. (이 클래스는 이전 QListView 클래스에서 제공했지만 Qt의 모델/뷰 아키텍처에서 제공하는 보다 유연한 접근 방식을 사용하여
# 표준 계층 목록을 제공하는데 사용됩니다.

# The QTreeView class is one of the Model/View Classes and is part of Qt's model/view framework.

# QTreeView는 QAbstractItemModel 클래스에 파생된 모델에서 제공하는 데이터를 표시할 수 있도록 QAbstractItemView 클래스에 의해 정의된
# 인터페이스를 구현합니다.

# It is simple to construct a tree view displaying data from a model. 다음 예에서 디렉토리의 내용은 QFileSystemModel에 의해
# 제공되고 트리로 표시됩니다.
#
# model = QFileSystemModel()
# model.setRootPath(QDir.currentPath())
#
# tree = QTreeView()
# tree.setModel(model)
#
# 모델/뷰 아키텍처는 모델이 변경될 때 트리 뷰의 내용이 업데이트 되도록 합니다.

# Items that have children can be in an expanded (children are visible) or collapsed (children are hidden) state.
# 이 상태가 변경되면 관련 항목의 모델 인덱스와 함께 축소() 또는 확장()신호가 방출됩니다.

# The amount of indentation used to indicate levels of hierarchy is controlled by the identation property.
# (계층 수준을 나타내는 데 사용되는 들여쓰기의 양은 들여쓰기 속성에 의해 제어됩니다.)

# 트리 뷰의 헤더는 QHeaderView 클래스를 사용하여 구성되면 header()->hide()를 사용하여 숨길 수 있습니다. 각 헤더는 true로 설정된
# stretchLastSection 속성으로 구성되어 뷰가 헤더에 할당된 공간을 낭비하지 않도록 합니다. if this value is set to true, this
# property will override the resize mode set on the last section in the header. (이 값이 true로 설정되면 이 속성은 헤더의
# 마지막 섹션에 설정된 크기 조정 모드를 재정의합니다.

# By default, all columns in a tree view are movable except the first. To disable movement of these columns,
# use QHeaderView's setSectionsMovable() function. 섹션 재정렬에 대한 자세한 내용은 헤더 섹션 이동을 참조하십시오.

# --- Improving Performance
# 많은 수의 항목을 표시할 때 성능을 향상시키기 위해 처리 중인 데이터에 대한 보기 힌트를 제공할 수 있습니다.
# 동일한 높이의 항목을 표시하기 위한 뷰에 대해 취할 수 있는 한 가지 접근 방식은 uniformRowHeights 속성을 true로 설정하는 것입니다.


import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pyqt.ConfigReader.IniReader import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle('Test Signal')

        self.reader = IniReader()

        # self.etc_load()
        # self.sys_load()
        self.read_ini()

    def read_ini(self):
        self.ini_file = './ini/yongdam.ini'
        self.sections = {
            'MANAGER': ['name', 'email', 'contact'],
            'NAC_MANAGER': ['name', 'email', 'contact'],
            'MSMT_SERVER': ['name', 'ip', 'port', 'dns', 'id', 'pwd'],
            'TM_SERVER': ['name', 'ip', 'port', 'id', 'pwd'],
            'SMART_TM': ['name', 'ip', 'port', 'id', 'pwd'],
            'DEVICE_SERVER': ['name', 'default_ip', 'ip', 'model', 'serial', 'id', 'pwd']
        }

        self.reader.setFile(self.ini_file)
        self.reader.setSections(self.sections)
        print(self.reader.read())


    def etc_load(self):
        absolute_path = QDir("C:/Shortcuts")    # Examples of absolute paths.
        relative_path = QDir("/images")  # Examples of absolute paths.
        # it = QDirIterator("/Shortcuts", QDirIterator.Subdirectories)
        it = QDirIterator(relative_path, QDirIterator.Subdirectories)
        while it.hasNext():
            print(it.next())


    def ini_load(self):
        ini_path = QDir("./ini/")


    def sys_load(self):
        # IteratorFlag
        # QDirIterator.NoIteratorFlags  :
        # QDirIterator.Subdirectories   :
        # QDirIterator.FollowSymlinks    :
        # it = QDirIterator("/Shortcuts", QDir.NoFilter, QDirIterator.Subdirectories | QDirIterator.FollowSymlinks)

        root_dir = QDir.root()
        root_dir.setFilter(QDir.Files | QDir.Hidden | QDir.NoSymLinks)
        root_dir.setSorting(QDir.Size | QDir.Reversed)

        for entry in root_dir.entryInfoList():
            print("{0}, {1}".format(entry.size(), entry.fileName()))

        print('---root dir---')
        print(root_dir.cd("Temp"))
        print(root_dir.currentPath())
        print(root_dir.dirName())
        absolute_dir_path = QDir("C:/Repo/tutorials/pyqt/images")    # Examples of absolute paths.
        relative_dir_path = QDir("./images")  # Examples of absolute paths.

        it = QDirIterator(relative_dir_path, QDirIterator.Subdirectories)
        # it = QDirIterator(absolute_dir_path, QDirIterator.Subdirectories)
        while it.hasNext():
            print('--start--')
            print(it.next())
            print(it.fileName())
            print(it.filePath())
            # QFileInfo ( https://doc.qt.io/qtforpython-5/PySide2/QtCore/QFileInfo.html#PySide2.QtCore.PySide2.QtCore.QFileInfo )
            print(it.fileInfo())
            # # f = QFile(it.next())
            # # f.open(QIODevice.ReadOnly)
            # # print("{0}, {1}".format(f.fileName(), f.readAll()))
            # f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
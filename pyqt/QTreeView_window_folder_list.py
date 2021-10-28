import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle('Window Folder')

        self.path_root = QDir.rootPath()
        self.model = QFileSystemModel()
        self.model.setRootPath(self.path_root)

        self.index_root = self.model.index(self.model.rootPath())

        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.index_root)
        self.tree_view.clicked.connect(self.on_treeView_clicked)

        self.setCentralWidget(self.tree_view)

    @pyqtSlot(QModelIndex)
    def on_treeView_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        print(fileName)
        print(filePath)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exit(app.exec())


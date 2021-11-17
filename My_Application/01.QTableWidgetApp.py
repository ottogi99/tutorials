# Ex. QTableWidget.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import pandas as pd
import numpy as np


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tableWidget = QTableWidget()
        self.tabs = QTabWidget()

        self.init_ui()
        self.setCentralWidget(self.tabs)

    def init_ui(self):
        self.init_menu_bar()

    # 파일 다이얼로그 설정
    def init_menu_bar(self):
        open_file = QAction(QIcon('../asset/open.png'), 'Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('새파일 열기')
        open_file.triggered.connect(self.show_dialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        file_menu = menubar.addMenu('&File')
        file_menu.addAction(open_file)

    # 테이블 위젯 설정
    def setTableWidget(self, df):
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

    def show_dialog(self):
        fileNames, selectedFilter = QFileDialog.getOpenFileNames(self, 'Open File', './data', "Comma (*.csv *.dat)")
        for idx, fileName in enumerate(fileNames):
            # 탭성하고 그 안에 표 출력하자(예정)
            print(fileName)
            # df = pd.read_csv(fileName, header=0, sep='\t')
            df = pd.read_csv(fileName, header=0)
            columnCount = len(df.columns)
            rowCount = len(df.values)
            print("column count:", columnCount)
            print("rowCount count:", rowCount)

            tab = QWidget()
            layout = QVBoxLayout()
            tableWidget = QTableWidget()
            # self.setTableWidget(df)

            tableWidget.setRowCount(rowCount)
            tableWidget.setColumnCount(columnCount)
            tableWidget.setHorizontalHeaderLabels(df.columns.values)
            tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            # # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
            # # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
            tableWidget.horizontalHeader()
            # # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)               # 헤더의 폭이 위젯의 폭에 맞춰지도록 합니다.
            # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)      # 헤더의 폭이 컨텐츠의 폭에 맞춰지도록 합니다.
            # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)    # 헤더의 폭이 항목 값의 폭에 맞춰지도록 합니다.
            tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)    # 헤더의 폭이 항목 값의 폭에 맞춰지도록 합니다.

            print(df)
            for i in range(rowCount):
                for j in range(columnCount):
                    print(df.iloc[i,j])
                    tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))


            layout.addWidget(tableWidget)
            tab.setLayout(layout)
            self.tabs.addTab(tab, 'Tab_'+str(idx))
        # self.tableWidget.setHorizontalHeaderLabels(df.columns.values)

        # vbox = QVBoxLayout()
        # vbox.addWidget(self.tableWidget)
        #
        # self.setLayout(vbox)
        #
        # self.setWindowTitle('QTableWidget')
        # self.setGeometry(300, 100, 600, 400)
        # self.show()

        # # print(os.path.abspath(path))
        # # # df = pd.read_csv(path)
        # # df = pd.read_csv(path, header=None, skiprows=1, nrows=1)
        # # names = df.values[0]
        # # df = pd.read_csv(path, header=None, names=names, skiprows=4)
        # # dfs.append((os.path.basename(path), df))
        # #
        # # pd.read_csv
        #
        # if fname[0]:
        #     f = open(fname[0], 'r', encoding='UTF8')
        #
        #     with f:
        #         data = f.read()
        #         self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    exit(app.exec())

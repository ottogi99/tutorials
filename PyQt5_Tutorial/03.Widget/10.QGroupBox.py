# Ex. QGroupBox.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.addWidget(self.create_first_exclusive_group(), 0, 0)
        grid.addWidget(self.create_second_exclusive_group(), 1, 0)
        grid.addWidget(self.create_non_exclusive_group(), 0, 1)
        grid.addWidget(self.create_push_button_group(), 1, 1)

        self.setLayout(grid)

        self.setWindowTitle('Box 02.Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def create_first_exclusive_group(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)

        v_box = QVBoxLayout()
        v_box.addWidget(radio1)
        v_box.addWidget(radio2)
        v_box.addWidget(radio3)
        groupbox.setLayout(v_box)

        return groupbox

    def create_second_exclusive_group(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        checkbox = QCheckBox('Independent Checkbox')
        checkbox.setChecked(True)

        v_box = QVBoxLayout()
        v_box.addWidget(radio1)
        v_box.addWidget(radio2)
        v_box.addWidget(radio3)
        v_box.addWidget(checkbox)
        v_box.addStretch(1)
        groupbox.setLayout(v_box)

        return groupbox

    def create_non_exclusive_group(self):
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True)

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)

        v_box = QVBoxLayout()
        v_box.addWidget(checkbox1)
        v_box.addWidget(checkbox2)
        v_box.addWidget(tristatebox)
        v_box.addStretch(1)
        groupbox.setLayout(v_box)

        return groupbox

    def create_push_button_group(self):
        groupbox = QGroupBox('Push Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        pushbutton = QPushButton('Normal Button')
        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True)
        popupbutton = QPushButton('Popup Button')

        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


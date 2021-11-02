# Ex. QDoubleSpinBox.

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl1 = QLabel('QDoubleSpinBox')
        self.dspinbox = QDoubleSpinBox()
        self.lbl2 = QLabel('$ 0.0')

        self.init_ui()

    def init_ui(self):
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix('$ ')
        self.dspinbox.setDecimals(1)
        self.dspinbox.valueChanged.connect(self.on_dspinbox_value_change)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.dspinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDoubleSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def on_dspinbox_value_change(self):
        self.lbl2.setText('$ ' + str(self.dspinbox.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    exit(app.exec())


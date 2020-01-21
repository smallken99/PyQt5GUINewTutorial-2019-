from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QSpinBox,QDial,QWidget,QVBoxLayout,QLabel

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QSpinValue"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "icon.png"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()

        self.spinBox = QSpinBox()
        self.spinBox.valueChanged.connect(self.spin_changed)
        vbox.addWidget(self.spinBox)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Sanserif',14))
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.show()

    def spin_changed(self):
        spinValue = self.spinBox.value()
        self.label.setText("Currerent Value is : {}".format(spinValue))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

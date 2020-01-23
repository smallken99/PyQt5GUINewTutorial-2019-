from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QToolBox,QLCDNumber,QSpinBox,QDial,QWidget,QVBoxLayout,QLabel

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 ToolBox"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "icon.png"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:yellow")
        self.initUI()
        self.show()

    def initUI(self):
        vbox = QVBoxLayout()

        toolbox = QToolBox()
        toolbox.setStyleSheet('background-color:green')
        toolbox.addItem(QLabel(), "Python")
        toolbox.addItem(QLabel(), "Java")
        toolbox.addItem(QLabel(), "C++")

        vbox.addWidget(toolbox)

        self.setLayout(vbox)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QLCDNumber,QSpinBox,QDial,QWidget,QVBoxLayout,QLabel

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
        self.title = "PyQt5 QLCDNumber"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "icon.png"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()
        self.show()

    def initUI(self):
        vbox = QVBoxLayout()

        self.lcd = QLCDNumber()
        self.lcd.setStyleSheet("background-color:green")
        # self.lcd.display(60)
        vbox.addWidget(self.lcd)
        self.button = QPushButton("Random Number Generator")
        self.button.setStyleSheet("background-color:yellow")
        self.button.clicked.connect(self.LCDHander)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def LCDHander(self):
        random = randint(1,200)
        self.lcd.display(random)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

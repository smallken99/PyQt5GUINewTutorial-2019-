from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QHBoxLayout,QLabel

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 WhatIsThis class"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 250
        self.iconName = "icon.png"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        hqbox = QHBoxLayout()
        label = QLabel("Focus and press SHIFT + F1")
        hqbox.addWidget(label)
        button = QPushButton("Check Me",self)
        button.setWhatsThis("This is a button that ...")
        hqbox.addWidget(button)
        self.setLayout(hqbox)
        self.show()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
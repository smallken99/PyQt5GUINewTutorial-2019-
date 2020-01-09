from PyQt5 import QtGui
from PyQt5.QtWidgets import QPushButton,QApplication,QGridLayout,QMainWindow,QDialog,QGroupBox,QHBoxLayout,QVBoxLayout

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Grid Layout"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 100
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def createLayout(self):
        # GROUP BOX 裝元件的群組
        self.groupBox = QGroupBox("What is your Favorite Programming Language?")

        gridlayout = QGridLayout()

        button = QPushButton("Python",self)
        button.setIcon(QtGui.QIcon("python.png"))
        button.setIconSize(QtCore.QSize(30,30))
        button.setMinimumHeight(40)
        gridlayout.addWidget(button,0,0)

        button1 = QPushButton("Java",self)
        button1.setIcon(QtGui.QIcon("java.png"))
        button1.setIconSize(QtCore.QSize(30,30))
        button1.setMinimumHeight(40)
        gridlayout.addWidget(button1,0,1)

        button2 = QPushButton(".NET",self)
        button2.setIcon(QtGui.QIcon("net.png"))
        button2.setIconSize(QtCore.QSize(30,30))
        button2.setMinimumHeight(40)
        gridlayout.addWidget(button2,1,0)

        button3 = QPushButton("PHP",self)
        button3.setIcon(QtGui.QIcon("php.png"))
        button3.setIconSize(QtCore.QSize(30,30))
        button3.setMinimumHeight(40)
        gridlayout.addWidget(button3,1,1)

        self.groupBox.setLayout(gridlayout)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
from PyQt5 import QtGui
from PyQt5.QtWidgets import QPushButton,QApplication, QMainWindow,QDialog,QGroupBox,QHBoxLayout,QVBoxLayout

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Window"
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
        self.groupBox = QGroupBox("What is your Favorite Sport?")

        hboxlayout = QHBoxLayout()

        button = QPushButton("Football",self)
        button.setIcon(QtGui.QIcon("football.png"))
        button.setIconSize(QtCore.QSize(30,30))
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        button1 = QPushButton("Cricket",self)
        button1.setIcon(QtGui.QIcon("cricket.png"))
        button1.setIconSize(QtCore.QSize(30,30))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button2 = QPushButton("Tennis",self)
        button2.setIcon(QtGui.QIcon("tennis.png"))
        button2.setIconSize(QtCore.QSize(30,30))
        button2.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        self.groupBox.setLayout(hboxlayout)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
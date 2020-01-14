from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QLabel,QDialog,QVBoxLayout

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Window"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "icon.png"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("football.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)

        self.show()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
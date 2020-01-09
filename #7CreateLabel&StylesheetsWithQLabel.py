from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QLabel,QDialog,QVBoxLayout

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Create Label & Stylesheets With QLabel"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        label = QLabel("This is PyQt5 Label")
        vbox.addWidget(label)

        labe2 = QLabel("This is PyQt5 GUI Application Development")
        labe2.setFont(QtGui.QFont("Sanserif",20)) # 設定字體、字型大小
        labe2.setStyleSheet("color:red") # 設定字顏色
        vbox.addWidget(labe2)
        self.setLayout(vbox)
        self.show()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QButtonGroup,QPushButton,QWidget,QLineEdit,QHBoxLayout,QLabel

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QButton Group"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "icon.png"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hqbox = QHBoxLayout()

        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif",14))
        hqbox.addWidget(self.label)

        button = QPushButton("Python")
        button.setFont(QtGui.QFont("Sanserif",14))
        button.setIcon(QtGui.QIcon("python.png"))
        button.setIconSize(QtCore.QSize(40,40))
        self.buttongroup.addButton(button,1)
        hqbox.addWidget(button)


        button2 = QPushButton("Java")
        button2.setFont(QtGui.QFont("Sanserif", 14))
        button2.setIcon(QtGui.QIcon("java.png"))
        button2.setIconSize(QtCore.QSize(40,40))
        self.buttongroup.addButton(button2,2)
        hqbox.addWidget(button2)

        button3 = QPushButton("PHP")
        button3.setFont(QtGui.QFont("Sanserif", 14))
        button3.setIcon(QtGui.QIcon("php.png"))
        button3.setIconSize(QtCore.QSize(40,40))
        self.buttongroup.addButton(button3,3)
        hqbox.addWidget(button3)


        self.setLayout(hqbox)
        self.show()

    def on_button_clicked(self,id):
        # 原始範例
        for button in self.buttongroup.buttons():
            if button  is self.buttongroup.button(id):
                self.label.setText(button.text() + " Was clicked.")

        # 我覺得也可以這樣寫
        # self.label.setText(self.buttongroup.button(id).text() + " Was clicked.")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
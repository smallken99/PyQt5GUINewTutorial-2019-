from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QLabel,QDialog,QVBoxLayout,QGroupBox,QRadioButton,QHBoxLayout

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Redio Button"
        self.left = 300
        self.top = 200
        self.width = 400
        self.height = 100
        self.iconName = "icon.png"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.radioButton()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif",13))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()


    def radioButton(self):
        self.groupBox = QGroupBox("What is your Favorite Sport?")
        self.groupBox.setFont(QtGui.QFont("Sanserif",13))
        hboxlayout = QHBoxLayout()

        self.radiobtn1 = QRadioButton("Football")
        self.radiobtn1.setIcon(QtGui.QIcon("football.png"))
        self.radiobtn1.setIconSize(QtCore.QSize(40,40))
        self.radiobtn1.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton("Cricket")
        self.radiobtn2.setIcon(QtGui.QIcon("cricket.png"))
        self.radiobtn2.setIconSize(QtCore.QSize(40,40))
        self.radiobtn2.setFont(QtGui.QFont("Sanserif",13))
        self.radiobtn2.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton("Tennis")
        self.radiobtn3.setIcon(QtGui.QIcon("tennis.png"))
        self.radiobtn3.setIconSize(QtCore.QSize(40,40))
        self.radiobtn3.setFont(QtGui.QFont("Sanserif",13))
        self.radiobtn3.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn3)


        self.groupBox.setLayout(hboxlayout)

    def OnRadioBtn(self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText("You Have selected " + radioBtn.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
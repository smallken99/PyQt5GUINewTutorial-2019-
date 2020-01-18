from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QGroupBox,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QRadioButton

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QGroupBox"
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


        groupbox = QGroupBox("Select your favorite Fruit?")
        groupbox.setFont(QtGui.QFont("Sanserif",14))

        vbox = QVBoxLayout()
        rad1 = QRadioButton("Apple")
        vbox.addWidget(rad1)

        rad2 = QRadioButton("Banana")
        vbox.addWidget(rad2)

        rad3 = QRadioButton("Melon")
        vbox.addWidget(rad3)

        groupbox.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(groupbox)

        self.setLayout(hbox)


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
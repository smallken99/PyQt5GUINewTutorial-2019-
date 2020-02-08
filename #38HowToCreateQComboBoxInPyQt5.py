from PyQt5.QtWidgets import QApplication,QDialog,QComboBox,QLabel,QVBoxLayout
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Combo Box')
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 100
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon("icon.png"))
        self.InitUI()
        self.show()

    def InitUI(self):
        vbox = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItem("Python")
        self.combo.addItem("Java")
        self.combo.addItem("C++")
        self.combo.addItem("C#")
        self.combo.addItem("Ruby")
        self.combo.currentTextChanged.connect(self.comboChanged)

        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif",15))
        self.label.setStyleSheet("color:red")

        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def comboChanged(self):
        text = self.combo.currentText()
        self.label.setText("You Have Selected: " + text)



if __name__ == "__main__":
    App = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(App.exec())
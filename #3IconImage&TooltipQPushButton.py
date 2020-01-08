from PyQt5.QtWidgets import QApplication,QPushButton,QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "PyQt5 Push button"
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = "icon.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left,top,width,height)
        self.UiComponets()
        self.show()

    def UiComponets(self):
        button = QPushButton("Click Me",self)
        # button.move(50,50)
        button.setGeometry(QRect(50,50,150,50))

        # 續 #2 前一範例
        button.setIcon(QtGui.QIcon("icon.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("按下確認鍵")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())



from PyQt5.QtWidgets import QApplication,QMainWindow, QDockWidget,QTextEdit,QListWidget
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class DockDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Dock Widget')
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon("icon.png"))
        self.createDockWidget()
        self.show()

    def createDockWidget(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        file.addAction("New")
        file.addAction("Save")
        file.addAction("Close")

        self.dock = QDockWidget("Dockable",self)
        self.listwidget = QListWidget()

        list = ["Python", "C++", "Java", "C#"]
        self.listwidget.addItems(list)
        self.dock.setWidget(self.listwidget)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    dockdialog = DockDialog()
    dockdialog.show()
    sys.exit(App.exec())
import sys
from PyQt5 import QtWidgets , QtGui ,  QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel
from PyQt5.uic.uiparser import QtWidgets
import untitled2
from untitled2 import *

class Box(QtWidgets.QMainWindow ,  untitled2.Ui_Form):
    def __init__(self):
        super(Box ,self).__init__()
        self.setupUi(self)
        self.label.hide()
        self.pushButton.clicked.connect(self.label.show)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Box()

    myapp.show()
    sys.exit(app.exec_())

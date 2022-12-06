import sys
from PyQt5 import QtWidgets , QtGui ,  QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel
from PyQt5.uic.uiparser import QtWidgets
import untitled3
from untitled3 import *
str='Обращение за подсказкой!'
class Box(QtWidgets.QMainWindow ,  untitled3.Ui_Form):
    def __init__(self):
        super(Box ,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clickMethod)
        self.pushButton.setToolTip("ЧАЙ КРУТОЙ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! КОФЕ ОТСТОЙ!!!!!!!!!!!!!")
    def clickMethod(self):
        print("Обращение за подсказкой!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Box()

    myapp.show()
    sys.exit(app.exec_())


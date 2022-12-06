import sys
from multiprocessing import connection
from PyQt5 import QtWidgets , QtGui ,  QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel
from PyQt5.uic.uiparser import QtWidgets
from matplotlib.dviread import Text
import untitled
from untitled import *
import matplotlib.pyplot as plt
import numpy as np
import math


class CoffeTea(QtWidgets.QMainWindow , untitled.Ui_Form):
    def __init__(self):
        super(CoffeTea ,self).__init__()
        self.setupUi(self)
        self.TeaText.hide()
        self.CoffeText.hide()
    def Prass_button(self):
        self.ButtonTea.clicked.connect(self.CoffeText.hide)
        self.ButtonTea.clicked.connect(self.TeaText.show)
    def Prass_button2(self):
        self.ButtonCoffe.clicked.connect(self.TeaText.hide)
        self.ButtonCoffe.clicked.connect(self.CoffeText.show)





if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = CoffeTea()
    myapp.show()
    myapp.Prass_button()
    myapp.Prass_button2()
    sys.exit(app.exec_())



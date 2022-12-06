import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QMainWindow, QPushButton
import matplotlib.pyplot as plt
import numpy as np
import math

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
x = np.arange(0, 10, 0.5)
y = (15-x-(np.cos(pow(x,3))/x))*np.sin(pow(x,3))

for i in range(0, len(x)):
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

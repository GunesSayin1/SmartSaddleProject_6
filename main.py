# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import pyqtgraph as pg
from PyQt5 import QtWidgets, uic,QtCore,QtGui
from pyqtgraph import PlotWidget, plot
import os
import sys
import pyqtgraph as pg
import pandas as pd

from util import BalanceDataProcessor

EXIT_CODE_REBOOT =  -1073740791
uiDesignFilePath = 'uiDesign.ui'
xChange=[]
balanceDataProcessor = BalanceDataProcessor()
filepath=""

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        loadUi(uiDesignFilePath, self)

        self.setWindowTitle("Smart Saddle")


       # self.pushButton.clicked.connect(self.show_scatterplot(xList, yList))

        #Import CSV Button
        #btn1 = QtWidgets.QPushButton('Import CSV', self)
        #btn1.resize(btn1.sizeHint())



       # self.show_scatterplot()
        self.pushButton_2.clicked.connect(self.show_scatterplottest)
        self.pushButton.clicked.connect(self.getCSV)


        print(balanceDataProcessor._calc_score())


    def show_scatterplot(self,xList,yList):

        # Get the balance data

        # Create pyqtgraph plot window
        #pltwindow = pg.plot(xList, yList, pen=None, symbolPen=None, symbolSize=8)

        #pltwindow.setWindowTitle('Heatmap')
        self.graphWidget.clear()
        StringScore = str(balanceDataProcessor.get_score())
        self.graphWidget.plot(xList,yList,pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50))
        self.textBrowser.append("Balance Score : "+ StringScore)


    def show_scatterplottest(self):
        balanceDataProcessor.__init__()
        print(balanceDataProcessor.get_score())
        xList = balanceDataProcessor.get_balance_data()['xChange']
        yList = balanceDataProcessor.get_balance_data()['yChange']
        self.show_scatterplot(xList, yList)




    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if filePath != "":
            print (filePath)
            #self.df = pd.read_csv(str(filePath))
            #print(self.df)
            with open("copy.txt", "w") as file:
                file.write(str(filePath))


if __name__ == "__main__":

    # Set graph background settings
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')

    # Start interface
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
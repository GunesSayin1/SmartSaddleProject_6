# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from util import BalanceDataProcessor

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)


import pyqtgraph as pg

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
class MatplotlibWidget(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        loadUi("qt_designer2.ui", self)

        self.setWindowTitle("PyQt5 & Matplotlib Example GUI")

        self.pushButton.clicked.connect(self.update_graph)



        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))


    def update_graph(self):
        balanceDataProcessor = BalanceDataProcessor()

        x = balanceDataProcessor.balanceDataDF['timestamp']
        y = balanceDataProcessor.balanceDataDF['xChange']
        y2 = balanceDataProcessor.balanceDataDF['yChange']

        # create plot
        plt = pg.plot()
        plt.showGrid(x=True, y=True)
        plt.addLegend()

        # set properties
        plt.setLabel('left', 'Value', units='V')
        plt.setLabel('bottom', 'Time', units='s')
        plt.setWindowTitle('pyqtgraph plot')

        # plot
        c1 = plt.plot(x, y, pen='b',name='xChange')
        c2 = plt.plot(x, y2, pen='r', name='yChange')

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()


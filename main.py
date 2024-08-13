import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtCore
import pyqtgraph as pg
from random import randint, random


uiclass, baseclass = pg.Qt.loadUiType("./UI/main_ui.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plot(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Hours
            [30, 32, 34, 32, 33, 31, 29, 32, 35, 45],  # Temperature
        )
        self.time = list(range(10000))
        self.temperature = [randint(0, 100) for _ in self.time]
        self.tim = QtCore.QTimer()
        self.tim.setInterval(1000)
        styles = {"color": "red", "font-size": "18px"}
        self.graphWidget_constellation.setLabel("bottom", "Q")
        self.graphWidget_constellation.setLabel("left", "I")
        self.graphWidget_constellation.addLegend()
        self.graphWidget_constellation.showGrid(x=True, y=True)
        self.graphWidget_constellation.setXRange(0, 1)
        self.graphWidget_constellation.setYRange(0, 1)
        self.tim.timeout.connect(self.update_plot2)
        self.tim.start()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def plot(self, hour, temperature):
        self.graphWidget_FFT.plot(hour, temperature)
        self.graphWidget_constellation.plot(hour, temperature)
    #     self.graphWidget_time.plot(hour, temperature)


    def update_plot2(self):
        self.temperature = [random() for _ in range(2)]
        self.graphWidget_constellation.plot(range(2), self.temperature)

    def update_plot(self):
        self.temperature = [randint(0, 100) for _ in self.time]
        self.graphWidget_time.clear()
        self.graphWidget_time.plot(self.time, self.temperature)

    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
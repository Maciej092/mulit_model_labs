import sys
import numpy as np
import random
import matplotlib.animation as animation
from PyQt5.QtWidgets import QLineEdit, QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Cellular automata - pyqt5'
        self.width = 640
        self.height = 400
        self.playing = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.canvas = PlotCanvas(self, width=5, height=4)
        self.canvas.move(0, 0)
        self.set_range = 500
        self.data = np.array([[np.zeros(3) for y in range(self.set_range)] for x in range(self.set_range)])
        self.canvas.ax = plt.imshow(self.data, animated=True)
        self.canvas.draw()

        # Create buttons
        self.button_start = QPushButton('Start', self)
        self.button_start.setToolTip('This s an example button')
        self.button_start.move(500, 0)
        self.button_start.resize(140, 30)
        self.button_start.clicked.connect(self.start)

        self.button_stop = QPushButton('Stop', self)
        self.button_stop.setToolTip('This s an example button')
        self.button_stop.move(500, 35)
        self.button_stop.resize(140, 30)
        self.button_stop.clicked.connect(self.start)

        self.button_clear = QPushButton('Clear space', self)
        self.button_clear.setToolTip('This s an example button')
        self.button_clear.move(500, 70)
        self.button_clear.resize(140, 30)
        self.button_clear.clicked.connect(self.clear)

        self.button_step = QPushButton('Step', self)
        self.button_step.setToolTip('This s an example button')
        self.button_step.move(500, 105)
        self.button_step.resize(140, 30)
        self.button_step.clicked.connect(self.step)

        # Create Line edit widget
        self.textbox = QLineEdit('Enter the space size', self)
        self.textbox.move(500, 140)
        self.textbox.resize(140, 30)
        self.textbox.returnPressed.connect(self.start)
        self.show()

    # def init(self):
    #     self.canvas.ax.set_data(self.data)
    #     return [self.canvas.ax]

    @pyqtSlot()
    def start(self):
        if self.playing:
            pass
        else:
            self.playing = True
            self.ani = animation.FuncAnimation(
                self.canvas.figure,
                self.update_space,
                blit=False, interval=25
            )

    def update_space(self, i):
        x = 100
        y = 100
        self.canvas.ax.imshow(self.f(x, y))
        return self.canvas.ax,

    def f(self, x, y):
        data = np.array([[[random.random(), random.random(), random.random()]
                          for item in range(y)] for itemm in range(x)])
        return data

    @pyqtSlot()
    def stop(self):
        if self.playing:
            self.playing = False
            self.ani._stop()
        else:
            pass

    # def stop(self):
    #     self.set_range = 500
    #     data = np.array(
    #         [[[random.random(), random.random(), random.random()] for y in range(self.set_range)] for x in
    #          range(self.set_range)])
    #     self.ax = self.figure.add_subplot()
    #     self.ax.imshow(data)
    #     self.ax.set_title('Cellular automata')
    #     self.draw()

    @pyqtSlot()
    def step(self):
        self.ani = animation.FuncAnimation(self.canvas.figure, self.start, blit=True, interval=25)
        self.draw()

    @pyqtSlot()
    def clear(self):
        self.set_range = 500
        data = np.array([[np.zeros(3) for y in range(self.set_range)] for x in range(self.set_range)])
        self.canvas.ax = self.canvas.figure.add_subplot()
        self.canvas.ax.imshow(data)
        self.canvas.ax.set_title('Cellular automata')
        self.canvas.draw()


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

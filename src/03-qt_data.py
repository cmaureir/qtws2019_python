import sys
import pandas as pd

from PySide2.QtWidgets import (QMainWindow, QApplication, QHBoxLayout,
                               QWidget, QVBoxLayout)
from QtPandas import QDataFrame
from QtMatplotlib import Canvas, Toolbar, Plot, Figure


class Window(QMainWindow):
    def __init__(self, df=None, parent=None):
        QMainWindow.__init__(self, parent)

        # Central widget
        self._main = QWidget()
        self.setCentralWidget(self._main)

        # Plot
        self.fig = Figure()
        self.canvas = Canvas(self.fig)

        # Table
        self.qdf = QDataFrame(df)

        # Right layout
        rlayout = QVBoxLayout()
        rlayout.addWidget(self.qdf)

        # Main layout
        layout = QHBoxLayout(self._main)
        layout.addWidget(self.canvas, 1)
        layout.addLayout(rlayout, 1)

        # MainWindow toolbar
        self.addToolBar(Toolbar(self.canvas, self))

        self.x = self.qdf.df["time"]
        self.y = self.qdf.df["mag"]

        self.plot_data(self.x, self.y)

    def plot_data(self, x, y):
        return Plot(self.canvas, x, y, marker="-")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window(df=pd.read_csv("month.csv"))
    w.show()
    sys.exit(app.exec_())

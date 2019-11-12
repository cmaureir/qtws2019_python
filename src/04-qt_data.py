import sys
import pandas as pd

from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import (QMainWindow, QApplication, QHBoxLayout,
                               QWidget, QComboBox, QVBoxLayout, QGridLayout,
                               QLabel)
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

        # Axis selection
        axis_layout = self.setup_axis_layout()

        # Right layout
        rlayout = QVBoxLayout()
        rlayout.addLayout(axis_layout)
        rlayout.addWidget(self.qdf)

        # Main layout
        layout = QHBoxLayout(self._main)
        layout.addWidget(self.canvas, 1)
        layout.addLayout(rlayout, 1)

        # MainWindow toolbar
        self.addToolBar(Toolbar(self.canvas, self))

        self.x = self.qdf.df["time"]
        self.y = None

    def plot_data(self, x, y):
        return Plot(self.canvas, x, y, marker="-")

    def setup_axis_layout(self):
        layout = QGridLayout()
        self.combo_x = QComboBox()
        self.combo_y = QComboBox()

        self.combo_x.currentTextChanged.connect(self.update_plot_x)
        self.combo_y.currentTextChanged.connect(self.update_plot_y)

        self.combo_x.addItem(self.qdf.columns()[0])
        self.combo_y.addItems(self.qdf.columns()[1:])
        self.combo_x.setEnabled(False)

        layout.addWidget(QLabel("X axis data:", alignment=Qt.AlignVCenter), 0, 0)
        layout.addWidget(QLabel("Y axis data:", alignment=Qt.AlignVCenter), 1, 0)
        layout.addWidget(self.combo_x, 0, 1)
        layout.addWidget(self.combo_y, 1, 1)
        return layout

    def update_plot(self):
        try:
            self.fig.clf()
            self._ax = self.plot_data(self.x, self.y)
        except:
            print("invalid data")

    @Slot()
    def update_plot_x(self, text):
        self.x = self.qdf.df[text].tolist()
        self.update_plot()

    @Slot()
    def update_plot_y(self, text):
        self.y = self.qdf.df[text].tolist()
        self.update_plot()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window(df=pd.read_csv("month.csv"))
    w.show()
    sys.exit(app.exec_())

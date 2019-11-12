import sys
import pandas as pd

from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from QtPandas import QDataFrame


class Window(QMainWindow):
    def __init__(self, df=None, parent=None):
        QMainWindow.__init__(self, parent)

        # Central widget
        self._main = QWidget()
        self.setCentralWidget(self._main)

        # Table
        self.qdf = QDataFrame(df)

        layout = QVBoxLayout(self._main)
        layout.addWidget(self.qdf)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window(df=pd.read_csv("month.csv"))
    w.show()
    sys.exit(app.exec_())

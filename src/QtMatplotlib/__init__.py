from PySide2.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure as MatplotlibFigure

def Figure(fig_size=(5,3)):
    return MatplotlibFigure(figsize=fig_size)

def Canvas(figure):
    return FigureCanvas(figure)

def Toolbar(canvas, parent):
    return NavigationToolbar2QT(canvas, parent)

def Plot(canvas, x, y, marker="-"):
    #ax = canvas.figure.subplots()
    ax = canvas.figure.add_subplot()
    #ax.plot(x, y, marker)
    ax.plot_date(x, y, marker)
    ax.xaxis.set_tick_params(rotation=30, labelsize=7)
    canvas.draw()
    return ax

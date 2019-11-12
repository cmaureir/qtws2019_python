# Qt World Summit 2019 Berlin
## Write Your First Data-based Application with Qt for Python in 0.01 days

Handling data is a fun task, but it can easily become a messy one.

Thankfully Python helps us to solve most of our problems,
due to the large amount of modules that improve our workflow,
but having a set of scripts, that can help you on different processes,
is not the best way to distribute or allow other users to use them.

Getting value from your code base usually translates into adapting it into
a more easy-to-understand process including: allowing to select input files,
change parameters, save plots, etc.

This new layer of difficulty is more extreme if the end-user of your script
is someone without Python or programming knowledge.

In this talk, you will learn how to create data-oriented graphical user
interfaces, to make algorithms easier to use.

### Example

The code used for the example is inspired on the content of the second
[Qt for Python Webinar](https://www.youtube.com/watch?v=wKqLaNqxgas),
from which you can find a
[step-by-step tutorial](https://doc.qt.io/qtforpython/tutorials/datavisualize/index.html)
on the official docs.

The motivation was that there is currently a lot of boilerplate code
that needs to be written to achieve writing a simple application from scratch,
so we showed one of the alternatives for improving such situation.

Inside the [src](src/) directory you will find the following contents.

First example:
* [Qt for Python: Hello World](src/hello.py)

Modules:
* [QtMatplotlib](src/QtMatplotlib/), module that provide a couple of abstractions
  for a Matplotlib Canvas and a Figure, so it can be easily used by a Qt application.
* [QtPandas](src/QtPandas/), proof-of-concept module that expose a QDataFrame class
  which automatically handle a Pandas DataFrame into a QTableView + Model.

Live example:
* [Earthquake data](src/month.csv)
* [Qt Data application (01)](src/01-qt_data.py), empty QMainWindow.
* [Qt Data application (02)](src/02-qt_data.py), DataFrame values displayed
  inside the QDataFrame module.
* [Qt Data application (03)](src/03-qt_data.py), table and plot of the DataFrame data.
* [Qt Data application (04)](src/04-qt_data.py), final example that provides also
  a way to change the y-axis column that is currently plotted.

### Slides

You can check the [slides here!](https://maureira.xyz/talks/qt/qtws2019_python)
to write them I used [reveal.js](https://github.com/hakimel/reveal.js/).

from PySide2.QtWidgets import QWidget, QTableView, QHBoxLayout, QHeaderView
from PySide2.QtCore import QAbstractTableModel, QModelIndex, Qt


class QDataFrameTableModel(QAbstractTableModel):
    def __init__(self, df=None):
        QAbstractTableModel.__init__(self)
        self.df = df
        self.row_count = self.df.shape[0]
        self.column_count = self.df.shape[1]

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return list(self.df.columns)[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()
        if role == Qt.DisplayRole:
            value = "{}".format(self.df.iloc[row][column])
            return value
        return None


class QDataFrame(QWidget):
    def __init__(self, df=None, parent=None):
        QWidget.__init__(self, parent)
        self.df = df

        self.model = QDataFrameTableModel(self.df)

        self.table_view = QTableView()
        #self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.table_view.setModel(self.model)

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.table_view)
        self.setLayout(self.main_layout)
    def columns(self):
        return self.df.columns.tolist()

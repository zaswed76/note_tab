import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class LabelItem(QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.select_flag = False


    def mousePressEvent(self, QMouseEvent):
        self.select_flag = not self.select_flag
        if self.select_flag:
            self.setStyleSheet("QLabel {color: #51D731;}")
        else:
            self.setStyleSheet("QLabel {color: #636363;}")

    def enterEvent(self, *args, **kwargs):
        self.setToolTip("0.86")

class Column(QFrame):
    def __init__(self):
        super().__init__()
        self.main_box = QVBoxLayout(self)
        self.main_box.setContentsMargins(0, 0, 0, 0)
        self.main_box.setSpacing(6)

    def add_item(self, item):
        self.main_box.addWidget(item, alignment=Qt.AlignLeft | Qt.AlignTop)

    def add_stretch(self, s):
        self.main_box.addStretch(s)

class Table(QFrame):
    def __init__(self):
        super().__init__()
        self._data = None
        self.main_hbox = QHBoxLayout(self)
        self.columns = {}

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def update_table(self):
        self.clearLayout(self.main_hbox)

        if self.data is not None:
            for n, col in enumerate(self.data):
                self.columns[n] = Column()
                self.main_hbox.addWidget(self.columns[n])
                for w in col:
                    self.columns[n].add_item((LabelItem(w[0])))
                self.columns[n].add_stretch(1)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())


    def sort_by(self, sorter):
        return sorter(self.data)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("../css/style.css", "r").read())
    main = Table()
    main.show()
    data = [[("w", 1), ("w2", 2)], [("w3", 3), ("w4", 4)], [("w5", 5), ("w6", 6)]]
    main.data = data
    main.update_table()

    sys.exit(app.exec_())
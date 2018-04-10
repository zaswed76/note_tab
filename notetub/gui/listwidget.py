
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *

class ListView(QListView):
    def __init__(self, model):
        super().__init__()
        self.setModel(model)
        # self.setAlternatingRowColors(True)
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionRectVisible(False)
        # self.setGridSize(QSize(55, 45))


class ListModel(QStandardItemModel):
    def __init__(self):
        super().__init__()

    def set_items(self, items):
        self.clear()
        for i in items:
            item = QStandardItem(str(i))
            self.appendRow(item)



if __name__ == "__main__":

    from notetub.ex import serv
    app = QApplication(sys.argv)



    model = ListModel()
    mw = ListView()
    mw.setModel(model)

    app.setStyleSheet(open("../css/style.css", "r").read())

    words = serv.group_by(serv.get_words("../resources/words.txt"), 10)
    print(words[0])
    model.set_items(words[0])
    model.set_items(words[0])

    mw.show()
    sys.exit(app.exec())
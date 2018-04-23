
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *

class StandardItem(QStandardItem):
    def __init__(self, text, ratio, ratio_in_text=False, ndigits=3):

        super().__init__()
        ratio = str(round(ratio, ndigits))
        if ratio_in_text:
            text = "{} {}".format(text, ratio)
        else:
            self.setToolTip(ratio)

        self.setText(text)


class ListView(QListView):
    def __init__(self, model):
        super().__init__()
        self.setModel(model)
        # self.setAlternatingRowColors(True)
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionRectVisible(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # self.setSizePolicy(sizePolicy)


class ListModel(QStandardItemModel):
    def __init__(self):
        super().__init__()

    def set_items(self, items):
        self.clear()
        for i, r in items:
            item = StandardItem(i, r)

            self.appendRow(item)



if __name__ == "__main__":

    from notetub.lib import serv
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
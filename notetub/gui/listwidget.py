import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *


class CustomItem(QLabel):
    def __init__(self, text, ratio, ratio_in_text=True, ndigits=3,
                 tool_tip=False, *__args):
        super().__init__(*__args)
        ratio = str(round(ratio, ndigits))
        if ratio_in_text:
            text = "{} {}".format(text, ratio)
        elif tool_tip:
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




class ListWidget(QListWidget):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg

    def set_items(self, items):
        ratio_in_text = self.cfg["ratio_in_text"]
        ndigits = self.cfg["ndigits"]
        tool_tip = self.cfg["tool_tip"]

        self.clear()
        for i, r in items:
            item = CustomItem(i, r, ratio_in_text=ratio_in_text,
                                ndigits=ndigits,
                                tool_tip=tool_tip)

            self.setItemWidget(QListWidgetItem(self), item)


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

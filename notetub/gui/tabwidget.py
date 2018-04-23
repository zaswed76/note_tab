# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *


from notetub.gui.listwidget import *

class TableList(QFrame):
    def __init__(self):
        super().__init__()
        self.box = QHBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.lst_models = []
        self.max_column_size_list = []
        self.max_line_size_list = []


    def set_items(self, items_list):
        for n, lst in enumerate(items_list):
            model = ListModel()
            model.set_items(lst)
            self.lst_models.append(model)
            view = ListView(model)
            self.max_column_size_list.append(view.sizeHintForColumn(0))
            self.max_line_size_list.append(view.sizeHintForRow(0))
            self.box.addWidget(view)

    @property
    def max_column_size(self):
        return max(self.max_column_size_list)

    @property
    def max_line_size(self):
        return max(self.max_line_size_list)

    def clear_table(self):

        for m in self.lst_models:
            print(m, 111)
            m.clear()


if __name__ == '__main__':
    from notetub.lib import serv
    app = QApplication(sys.argv)
    app.setStyleSheet(open("../css/style.css", "r").read())
    main = TableList()
    main.resize(100, 100)
    # words = serv.group_by(serv.get_words("../resource/dictionaries/corpora_noun.txt", 100), 20)
    # main.set_items(words)
    main.show()
    sys.exit(app.exec_())
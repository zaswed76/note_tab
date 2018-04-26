# -*- coding: utf-8 -*-

import sys

import sip
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *


from notetub.gui.listwidget import *

class TableList(QFrame):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.box = QHBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.lst_models = []
        self.max_column_size_list = []
        self.max_line_size_list = []
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def sort_by(self, sorter):
        self.data = sorter(self.data)

    def group_by(self, grouper, count=None):
        self.data = grouper(self.data, count)

    def update_table(self):
        for n, lst in enumerate(self._data):
            list_widget = ListWidget(self.cfg)
            list_widget.set_items(lst)
            self.lst_models.append(list_widget)

            # self.max_column_size_list.append(self.sizeHintForColumn(0))
            # self.max_line_size_list.append(self.sizeHintForRow(0))
            self.box.addWidget(list_widget)

    @property
    def max_column_size(self):
        return max(self.max_column_size_list)

    @property
    def max_line_size(self):
        return max(self.max_line_size_list)

    def clear_table(self):
        for m in self.lst_models:

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
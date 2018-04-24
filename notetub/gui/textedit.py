

import sys
from PyQt5.QtWidgets import *

class TextEdit(QTextEdit):
    def __init__(self, *__args):
        super().__init__(*__args)

    def set_items(self, items):
        for i in items:
            self.append(i)

class TableList(QFrame):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.box = QHBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.lst_models = []



    def set_items(self, items_list):
        for n, lst in enumerate(items_list):
            view = TextEdit()
            self.lst_models.append(view)
            view.set_items(lst)
            self.box.addWidget(view)

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
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = TextEdit()
    main.append("111111")
    main.append("111111")
    main.show()
    sys.exit(app.exec_())
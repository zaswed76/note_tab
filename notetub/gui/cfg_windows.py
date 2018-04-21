

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Combo(QComboBox):
    def __init__(self):
        super().__init__()


class QSpin(QSpinBox):
    def __init__(self):
        super().__init__()

class AbcCfgWidget(QLabel):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(name)
        self.setStyleSheet("background-color: #CCCCCE")



class SearchCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.box = QVBoxLayout(self)


        self.algorithm_group = QGroupBox()
        self.check_valid_line = QCheckBox()









class TableCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.box_grid = QGridLayout(self)
        self.all_words = QSpin()
        self.all_words.setValue(cfg["max_words"])
        self.box_grid.addWidget(QLabel("найденных слов"), 0, 0)
        self.box_grid.addWidget(self.all_words, 0, 1)

        self.words_on_page = QSpin()
        self.words_on_page.setValue(cfg["words_on_page"])
        self.box_grid.addWidget(QLabel("слов на странице"), 1, 0)
        self.box_grid.addWidget(self.words_on_page, 1, 1)


        self.columns = QSpin()
        self.columns.setValue(cfg["number_columns"])
        self.box_grid.addWidget(QLabel("колонок"), 2, 0)
        self.box_grid.addWidget(self.columns, 2, 1)



        self.box_grid.setRowStretch(3, 1)



class ViewCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())


import sys


from PyQt5.QtWidgets import *


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

class RadioButton(QRadioButton):
    def __init__(self, *__args):
        super().__init__(*__args)

class Algorithms(QGroupBox):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.algorithms = {}
        self.box = QVBoxLayout()
        self.setLayout(self.box)

    def add_algorithm(self, name):
        self.algorithms[name] = RadioButton(name)
        self.box.addWidget(self.algorithms[name])

    def set_active_algorithm(self, name):
        self.algorithms[name].setChecked(True)

    def get_active_algorithm(self):
        for n, r in self.algorithms.items():
            if r.isChecked():
                return n

class SearchCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.cfg = cfg
        self.main_box = QVBoxLayout(self)
        self.__init_algorithms()
        self.main_box.addStretch(1)

    def __init_algorithms(self):
        self.algorithm_box = Algorithms("алгоритмы")
        self.main_box.addWidget(self.algorithm_box)
        for alg in self.cfg["algorithm_list"]:
            self.algorithm_box.add_algorithm(alg)
        self.algorithm_box.set_active_algorithm(self.cfg["search_algorithm"])

class LightingCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)




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

class CheckDict(QCheckBox):
    def __init__(self, *__args):
        super().__init__(*__args)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import *
from os.path import basename, splitext
from notetub.gui.cfg_windows import AbcCfgWidget, CheckDict

class DictCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.all_dicts = [splitext(basename(x))[0] for x in cfg["dictionaries_files"]]
        self.works_dictionaries = cfg["works_dictionaries"]
        self.all_check_dictionaries = {}
        self.main_box = QVBoxLayout(self)
        self.__init_check_dict()
        self.main_box.addStretch(1)
        self.__init_active_dict()

    def __init_check_dict(self):
        for d in self.all_dicts:
            self.all_check_dictionaries[d] = CheckDict(d)
            self.main_box.addWidget(self.all_check_dictionaries[d])

    def __init_active_dict(self):
        for d in self.works_dictionaries:
            if d in self.all_check_dictionaries:
                self.all_check_dictionaries[d].setChecked(True)

    @property
    def get_active_dict(self):
        return [x for x in self.all_check_dictionaries.values() if x.isChecked()]
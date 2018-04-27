
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os.path import basename, splitext
from notetub.gui.cfg_windows import AbcCfgWidget, CheckDict

class ListItem(QListWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setCheckState(Qt.Unchecked)
        # self.setSelected(True)



class Tools(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_box = QVBoxLayout(self)

        self.add_btn = QPushButton("add")
        self.del_btn = QPushButton("del")
        self.edit_btn = QPushButton("edit")
        self.add_to_btn = QPushButton("add to")
        self.del_from_btn = QPushButton("del from")
        self.main_box.addWidget(self.add_btn)
        self.main_box.addWidget(self.del_btn)
        self.main_box.addWidget(self.edit_btn)
        self.main_box.addWidget(self.add_to_btn)
        self.main_box.addWidget(self.del_from_btn)
        self.main_box.insertStretch(-1, 1)

class DictList(QListWidget):
    def __init__(self):
        super().__init__()

    def add_items(self, *items):
        for line in items:
            item = ListItem(line)
            self.addItem(item)




class DictCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.all_dicts = [splitext(basename(x))[0] for x in cfg["dictionaries_files"]]
        self.works_dictionaries = cfg["works_dictionaries"]
        self.all_check_dictionaries = {}
        self.main_box = QHBoxLayout(self)
        self.dict_box = QVBoxLayout()
        self.tool_box = QVBoxLayout()

        self.tools = Tools()
        self.dict_list = DictList()
        self.main_box.addWidget(self.dict_list)
        self.main_box.addWidget(self.tools)


        self.__init_check_dict()
        # self.main_box.addStretch(1)
        # self.__init_active_dict()





    def __init_check_dict(self):
        self.dict_list.add_items(*self.all_dicts)



    def __init_active_dict(self):
        for d in self.works_dictionaries:
            if d in self.all_check_dictionaries:
                self.all_check_dictionaries[d].setChecked(True)

    @property
    def get_active_dict(self):
        check_stub = CheckDict("corpora_noun")


        # return [x for x in self.all_check_dictionaries.values() if x.isChecked()]
        return [check_stub]
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os.path import basename, splitext
from notetub.gui.cfg_windows import AbcCfgWidget, CheckDict
from notetub.lib import serv

class ListItem(QListWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|
                      Qt.ItemIsSelectable)
        self.setCheckState(Qt.Unchecked)


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

    def add_item(self, item):
        self.addItem(ListItem(item))

    def remove_item(self, item):
        self.takeItem(self.indexFromItem(item).row())


class DictCfgWidget(AbcCfgWidget):
    def __init__(self, name, cfg, *args, **kwargs):
        super().__init__(name, cfg, *args, **kwargs)
        self.cfg = cfg
        self.all_dicts = [splitext(basename(x))[0] for x in
                          cfg["dictionaries_files"]]
        self.works_dictionaries = cfg["works_dictionaries"]
        self.all_check_dictionaries = {}
        self.main_box = QHBoxLayout(self)
        self.dict_box = QVBoxLayout()
        self.tool_box = QVBoxLayout()

        self.tools = Tools()
        self.dict_list_widget = DictList()
        self.main_box.addWidget(self.dict_list_widget)
        self.main_box.addWidget(self.tools)

        self.__init_check_dict()
        # self.main_box.addStretch(1)
        self.__init_active_dict()
        self.__init_controllers()

    def __init_check_dict(self):
        """
        отобразить все словари в каталоге
        """
        self.dict_list_widget.add_items(*self.all_dicts)

    def __init_active_dict(self):
        """
        включить активные
        """
        for d in self.works_dictionaries:
            items = self.dict_list_widget.findItems(d, Qt.MatchExactly)
            if items:
                items[0].setCheckState(Qt.Checked)


    @property
    def get_active_dict(self):
        checked_items = []
        for index in range(self.dict_list_widget.count()):
            if self.dict_list_widget.item(index).checkState() == Qt.Checked:
                checked_items.append(self.dict_list_widget.item(index))
        return checked_items

    def __init_controllers(self):
        self.tools.add_btn.clicked.connect(self.add_dict_file)
        self.tools.del_btn.clicked.connect(self.del_dict_file)

    def add_dict_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        if fname:
            item = serv.add_dict(fname, self.cfg["dictionaries_dir"], self.cfg["dictionary_ext"])

            self.dict_list_widget.add_item(item)

    def del_dict_file(self):
        del_item = self.dict_list_widget.selectedItems()[0]
        del_item_text = del_item.text()
        del_file = serv.del_dict(del_item_text, self.cfg["dictionaries_dir"], self.cfg["dictionary_ext"])
        if del_file is not None:
            self.dict_list_widget.remove_item(del_item)

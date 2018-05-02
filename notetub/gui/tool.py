
from PyQt5.QtWidgets import (QFrame, QHBoxLayout, QPushButton, QLineEdit,
                             QSpacerItem, QSizePolicy, QWidget)
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import QRegExp

from notetub.gui import customctrls

class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()





class ToolBtn(QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.setObjectName(name)

class CustomSpace(QFrame):
    def __init__(self, min_w=None, min_h=None):
        super().__init__()
        # self.setStyleSheet("background-color: green")
        if min_w is not None:

            self.setMinimumWidth(min_w)
        if min_h is not None:
            self.setMinimumHeight(min_h)


class Tool(QFrame):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.custom_groups = {}
        self.setFixedHeight(cfg["tool_height"])
        # self.setStyleSheet("background-color: lightgrey")

        self.box = QHBoxLayout(self)

        self.word_line = LineEdit()


        self.search_btn = ToolBtn("search")
        self.config_btn = ToolBtn("config")

        self.box.addWidget(self.word_line)
        self.box.addWidget(self.search_btn)
        self.box.addWidget(CustomSpace(min_w=10))
        # self.add_btn("uk")
        self.box.addStretch(1)



        self.box.addWidget(self.config_btn)
        #


    @property
    def line_edit_text(self):
        return self.word_line.text()


    def set_line_validator(self, reg=None):
        if reg is None:
            reg = "[\d\w!]+"
        validator = QRegExpValidator(QRegExp(reg))
        self.word_line.setValidator(validator)


    def set_custom_dict(self):
        controls = self.cfg.get("custom_controlls", {}).get("dictionaries", {})

        # if self.custom_groups.get("dict"):
        #     print()

        try:
            self.box.removeWidget(self.custom_groups["dict"])
            del(self.custom_groups["dict"] )
            print(controls, "controls111")
        except:
            pass
        print(len(controls), "len")
        if controls:
            print(777)
            self.custom_groups["dict"] = customctrls.CustomDictControls()
            self.box.insertWidget(3, self.custom_groups["dict"])
            print(controls.items(), "items")
            for n, ctrl in controls.items():
                self.custom_groups["dict"].add_control(ctrl["tag"])
            # self.box.removeWidget(self.custom_groups["dict"])


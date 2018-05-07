
from PyQt5.QtWidgets import (QFrame, QHBoxLayout, QPushButton, QLineEdit,
                             QSpacerItem, QSizePolicy, QWidget)
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import QRegExp

from notetub.gui import customctrls

class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()



class CustomButton(QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)


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
        self._selected_line_text = None
        self.setFixedHeight(cfg["tool_height"])
        # self.setStyleSheet("background-color: lightgrey")

        self.box = QHBoxLayout(self)

        self.word_line = LineEdit()
        self.word_line.selectionChanged.connect(self.set_select_text)


        self.search_btn = ToolBtn("search")
        self.config_btn = ToolBtn("config")

        self.box.addWidget(self.word_line)
        self.box.addWidget(self.search_btn)
        self.box.addWidget(CustomSpace(min_w=10))
        # self.add_btn("uk")
        self.box.addStretch(1)



        self.box.addWidget(self.config_btn)
        #

    def set_select_text(self):
        self.selected_line_text = self.word_line.selectedText()
        print(self.selected_line_text)

    @property
    def selected_line_text(self):
        return self._selected_line_text

    @selected_line_text.setter
    def selected_line_text(self, text):
        self._selected_line_text = text

    @property
    def line_edit_text(self):
        return self.word_line.text()


    def set_line_validator(self, reg=None):
        if reg is None:
            reg = "[\d\w!]+"
        validator = QRegExpValidator(QRegExp(reg))
        self.word_line.setValidator(validator)


    def set_custom_dict(self):

        self.custom_groups["dict"] = CustomButton("ru")
        self.box.insertWidget(3, self.custom_groups["dict"])



    def del_custom_dict(self):
        try:
            self.box.removeWidget(self.custom_groups["dict"])
        except KeyError:
            pass

    def selected_text(self):
        return self.word_line.selectedText()
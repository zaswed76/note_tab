
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import QRegExp

class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(38)
        font = QFont("serif", 18)
        self.setFont(font)



class ToolBtn(QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.setObjectName(name)


class Tool(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(50)
        self.setStyleSheet("background-color: lightgrey")

        self.box = QHBoxLayout(self)

        self.word_line = LineEdit()
        self.box.addWidget(self.word_line)

        self.search_btn = ToolBtn("search")
        self.config_btn = ToolBtn("config")



        self.box.addWidget(self.search_btn)
        self.box.addStretch(1)
        self.box.addWidget(self.config_btn)


    @property
    def line_edit_text(self):
        return self.word_line.text()




    def set_line_validator(self, reg=None):
        if reg is None:
            reg = "[\d\w!]+"
        validator = QRegExpValidator(QRegExp(reg))
        self.word_line.setValidator(validator)

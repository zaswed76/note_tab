
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont

class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(38)
        font = QFont("serif", 18)
        self.setFont(font)


class Tool(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(50)
        self.setStyleSheet("background-color: lightgrey")

        self.box = QHBoxLayout(self)

        self.word_line = LineEdit()
        self.box.addWidget(self.word_line)

        self.btn = QPushButton()
        self.box.addWidget(self.btn)


    @property
    def line_edit_text(self):
        return self.word_line.text()




        self.box.addStretch()

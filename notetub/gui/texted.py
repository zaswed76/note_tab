
import sys
from PyQt5.QtWidgets import *

class TextEdit(QTextEdit):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedHeight(26)


class TextEdit(QTextEdit):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedHeight(26)

class Widget(QFrame):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        self.box = QHBoxLayout(self)
        self.text_line = TextEdit()
        self.box.addWidget(self.text_line)
        self.btn = QPushButton()
        self.btn.clicked.connect(self.press)
        self.box.addWidget(self.btn)


    def press(self):
        self.text_line.setFocus()
        cursor = self.text_line.textCursor()
        textSelected = cursor.selectedText()
        print(textSelected)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open('style.css', "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())
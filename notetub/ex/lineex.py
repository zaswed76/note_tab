from PyQt5.QtWidgets import (QFrame, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout)

import sys
from PyQt5 import QtWidgets

class LineEdit(QLineEdit):
    def __init__(self, *__args):
        super().__init__(*__args)



class Window(QFrame):
    def __init__(self, *__args):
        super().__init__(*__args)
        box = QVBoxLayout(self)
        self.lned = LineEdit()
        self.btn = QPushButton()
        self.btn.clicked.connect(self.on_click)
        box.addWidget(self.lned)
        box.addWidget(self.btn)

    def on_click(self):
        print(self.lned.text())
        print(self.lned.selectedText())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('settings/style.qss', "r").read())
    main = Window()
    main.show()
    sys.exit(app.exec_())
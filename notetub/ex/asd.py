

import sys
from PyQt5 import QtWidgets

class Btn(QtWidgets.QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)





class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        box = QtWidgets.QHBoxLayout(self)
        self.btn = Btn(self)
        self.btn2 = Btn(self)

        box.addWidget(self.btn)
        box.addWidget(self.btn2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("style.css", "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())
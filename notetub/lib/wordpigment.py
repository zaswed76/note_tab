
import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Widget(QLabel):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        # font = QFont()
        # font.setFamily("helvetica")
        # font.setPointSize(18)
        # self.setFont(font)


class Pigment():
    def __init__(self):
        pass

    def pigment(self, line, pat, font):
        pass







if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    A = "<p>ко<font size=12 color=#636363 face=Helvetica Neue>ров</font>а</p>"
    main.setText(A)
    main.show()
    sys.exit(app.exec_())



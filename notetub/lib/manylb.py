import sys
from PyQt5 import QtWidgets

class Lb(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(5, 5)
        self.setStyleSheet("background-color: green")

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.box = QtWidgets.QGridLayout(self)
        self.box.setSpacing(1)
        self.box.setContentsMargins(1, 1, 1, 1)
        for y in range(310):
            for x in range(310):
                self.box.addWidget(Lb(), y, x)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())
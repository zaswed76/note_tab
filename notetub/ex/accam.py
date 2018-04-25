import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class LabelItem(QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.select_flag = False


    def mousePressEvent(self, QMouseEvent):
        self.select_flag = not self.select_flag
        if self.select_flag:
            self.setStyleSheet("QLabel {color: #51D731;}")
        else:
            self.setStyleSheet("QLabel {color: #636363;}")

    def enterEvent(self, *args, **kwargs):
        self.setToolTip("0.86")

class Column(QFrame):
    def __init__(self):
        super().__init__()
        self.main_box = QVBoxLayout(self)
        self.main_box.setContentsMargins(0, 0, 0, 0)
        self.main_box.setSpacing(6)

    def add_item(self, item):
        self.main_box.addWidget(item, alignment=Qt.AlignLeft | Qt.AlignTop)

    def add_stretch(self, s):
        self.main_box.addStretch(s)

class Table(QFrame):
    def __init__(self):
        super().__init__()
        self.main_box = QHBoxLayout(self)
        self.main_box.setSpacing(1)
        self.tool = QFrame()
        self.too_box = QVBoxLayout(self.tool)
        # self.tool.setStyleSheet("background-color: grey")
        self.tool.setFixedWidth(50)
        self.display = QFrame()
        self.display.setFixedWidth(300)
        self.display.setStyleSheet("background-color: lightgrey")
        self.main_box.addWidget(self.tool)
        self.main_box.addWidget(self.display, stretch=1)
        self.setFixedHeight(250)


        add_widget = QPushButton("add")
        add_widget.clicked.connect(self.add)
        remove_widget = QPushButton("del")
        remove_widget.clicked.connect(self.remove)

        self.too_box.addWidget(add_widget)
        self.too_box.addWidget(remove_widget)
        self.too_box.addStretch(1)

        self.display_box = QHBoxLayout(self.display)

        self.dynamic_widget = {}

    def add(self):
        self.remove()
        self.dynamic_widget = {}
        self.dynamic_widget["1"] = QFrame()
        self.dynamic_widget["1"].setStyleSheet("background-color: green")
        self.display_box.addWidget(self.dynamic_widget["1"])

    def remove(self):


        for i in reversed (range(self.display_box.count())):
            self.display_box.itemAt(i).widget().close()
            self.display_box.takeAt(i)
        if self.dynamic_widget:
            del(self.dynamic_widget)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("../css/style.css", "r").read())
    main = Table()
    main.show()


    sys.exit(app.exec_())
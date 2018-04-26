

import sys
from PyQt5.QtWidgets import *

class LabelItem(QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

class Widget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setItemWidget(QListWidgetItem(self), LabelItem("ttttttt"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())

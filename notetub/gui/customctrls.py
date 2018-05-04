import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DictCustomBtn(QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.setCheckable(True)
        self.setText(name)


class CustomDictControls(QComboBox):
    def __init__(self, *__args):
        super().__init__(*__args)

    def add_control(self, name):
        self.addItem(name)

    def del_control(self, name):
        i = self.findText(name, Qt.MatchExactly)
        if i > 0:
            self.removeItem(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = CustomDictControls()
    main.show()
    main.add_control("ru")
    main.add_control("uk")
    main.del_control("ru")
    print(main.controls)
    sys.exit(app.exec_())

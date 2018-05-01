import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *






class DictCustomBtn(QPushButton):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.setCheckable(True)
        self.setText(name)


class CustomDictControls(QGroupBox):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.group = QButtonGroup()
        self.controls = {}

        self.main_box = QHBoxLayout(self)
        self.main_box.setSpacing(5)
        self.main_box.setContentsMargins(0, 0, 0, 0)

    def add_control(self, name):
        self.controls[name] = DictCustomBtn(name)
        self.group.addButton(self.controls[name])
        self.main_box.addWidget(self.controls[name])


    def del_control(self, name):
        self.main_box.removeWidget(self.controls[name])

        self.group.removeButton(self.controls[name])
        del(self.controls[name])

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

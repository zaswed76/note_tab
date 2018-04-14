

import sys
from PyQt5.QtWidgets import *

class AbcCfgWidget(QLabel):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName(name)
        self.setStyleSheet("background-color: #CCCCCE")



class SearchCfgWidget(AbcCfgWidget):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)




class TableCfgWidget(AbcCfgWidget):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)

class ViewCfgWidget(AbcCfgWidget):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())
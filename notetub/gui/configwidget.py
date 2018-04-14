

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ConfigBtn(QPushButton):
    def __init__(self, name, text=None):
        super().__init__()
        self.setObjectName(name)
        self.setText(text)


class ConfigTool(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(100)
        self.vbox = QVBoxLayout(self)
        self.vbox.setContentsMargins(5, 0, 0, 0)
        self.vbox.setSpacing(6)
        self.__init_btns()

    def __init_btns(self):
        self.search_cfg_btn = ConfigBtn("search_cfg_btn", text="поиск")
        self.table_cfg_btn = ConfigBtn("table_cfg_btn", text="таблица")
        self.app_cfg_btn = ConfigBtn("app_cfg_btn", text="вид")
        self.vbox.addWidget(self.search_cfg_btn)
        self.vbox.addWidget(self.table_cfg_btn)
        self.vbox.addWidget(self.app_cfg_btn)
        self.vbox.addStretch(1)


class ConfigWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: 000000")



class AcceptFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: lightgrey")
        self.setFixedHeight(50)


class ConfigManager(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Настройки")
        self.setWindowFlags(Qt.Dialog)
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(500, 300)
        self.hbox = QHBoxLayout(self)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(0)
        self.tool = ConfigTool()
        self.hbox.addWidget(self.tool)
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        self.hbox.addLayout(vbox)

        self.config_widget = ConfigWidget()
        vbox.addWidget(self.config_widget)

        self.accept_frame = AcceptFrame()
        vbox.addWidget(self.accept_frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("../css/style.css", "r").read())
    main = ConfigManager()
    main.show()
    sys.exit(app.exec_())
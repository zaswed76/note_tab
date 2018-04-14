

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ConfigTool(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(100)


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


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from notetub.gui import cfg_windows

class ConfigBtn(QPushButton):
    def __init__(self, name, text=None):
        super().__init__()
        self._link_widget = None
        self.setObjectName(name)
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)
        self.setCheckable(True)

    @property
    def link_widget(self):
        return self._link_widget

    @link_widget.setter
    def link_widget(self, widget):
        self._link_widget = widget


class ConfigTool(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(100)
        self.vbox = QVBoxLayout(self)
        self.vbox.setContentsMargins(5, 0, 0, 0)
        self.vbox.setSpacing(6)
        self.tool_group = QButtonGroup()
        self.__init_btns()

    def __init_btns(self):
        self.search_cfg_btn = ConfigBtn("search_cfg_btn", text="поиск")
        self.table_cfg_btn = ConfigBtn("table_cfg_btn", text="таблица")
        self.app_cfg_btn = ConfigBtn("app_cfg_btn", text="вид")
        self.tool_group.addButton(self.search_cfg_btn)
        self.tool_group.addButton(self.table_cfg_btn)
        self.tool_group.addButton(self.app_cfg_btn)
        self.vbox.addWidget(self.search_cfg_btn)
        self.vbox.addWidget(self.table_cfg_btn)
        self.vbox.addWidget(self.app_cfg_btn)
        self.vbox.addStretch(1)


class ConfigWidget(QFrame):
    def __init__(self, cfg):
        super().__init__()

        self.setStyleSheet("background-color: 000000")
        self.stack = QStackedLayout(self)



        self.search_cfg = cfg_windows.SearchCfgWidget("search_cfg", cfg)
        self.table_cfg = cfg_windows.TableCfgWidget("table_cfg", cfg)
        self.view_cfg = cfg_windows.ViewCfgWidget("view_cfg", cfg)
        self.stack.addWidget(self.search_cfg)
        self.stack.addWidget(self.table_cfg)
        self.stack.addWidget(self.view_cfg)



class AcceptFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: lightgrey")
        self.setFixedHeight(50)


class ConfigManager(QFrame):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg

        self.setWindowTitle("Настройки")
        self.setWindowFlags(Qt.Dialog)
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(500, 300)
        self.hbox = QHBoxLayout(self)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(0)
        self.tool = ConfigTool()
        self.hbox.addWidget(self.tool)

        self.box_frame = QFrame()

        self.vbox = QVBoxLayout(self.box_frame)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(0)


        self.hbox.addWidget(self.box_frame)

        self.config_widget = ConfigWidget(cfg)
        self.vbox.addWidget(self.config_widget)

        self.accept_frame = AcceptFrame()
        self.vbox.addWidget(self.accept_frame)

        self.__init_controllers()


    def __init_controllers(self):
        self.tool.search_cfg_btn.clicked.connect(self.select_cfg_window)
        self.tool.search_cfg_btn.setChecked(True)
        self.tool.search_cfg_btn.link_widget = self.config_widget.search_cfg

        self.tool.table_cfg_btn.clicked.connect(self.select_cfg_window)
        self.tool.table_cfg_btn.link_widget = self.config_widget.table_cfg

        self.tool.app_cfg_btn.clicked.connect(self.select_cfg_window)
        self.tool.app_cfg_btn.link_widget = self.config_widget.view_cfg



    def select_cfg_window(self):
        self.config_widget.stack.setCurrentWidget(self.sender().link_widget)

    def closeEvent(self, *args, **kwargs):
        all_words = self.config_widget.table_cfg.all_words.value()
        words_on_page = self.config_widget.table_cfg.words_on_page.value()
        columns = self.config_widget.table_cfg.columns.value()

        self.cfg["max_words"] = all_words
        self.cfg["words_on_page"] = words_on_page
        self.cfg["number_columns"] = columns
        self.cfg["search_algorithm"] = self.config_widget.search_cfg.algorithm_box.get_active_algorithm()
        self.cfg.save()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("../css/style.css", "r").read())
    main = ConfigManager()
    main.show()
    sys.exit(app.exec_())
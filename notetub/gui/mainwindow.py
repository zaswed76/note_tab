import sys

from PyQt5.QtWidgets import QFrame, QApplication, QVBoxLayout
from PyQt5.QtCore import *

from notetub.gui import wizard, tool
from notetub.lib import serv, sorter
from notetub.morphlibs import _diff


def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
        mode = 'INFO'
    elif mode == QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))

qInstallMessageHandler(qt_message_handler)

class Controller:
    def __init__(self, parent):
        self.parent = parent

    def enter(self):
        self.parent.set_omo_words()

    def open_config(self):
        self.parent.show_config_manager()


class MainWindow(QFrame):
    def __init__(self, cfg):
        super().__init__()
        qDebug('something informative')
        self.controller = None
        self.config_manager = None
        self.cfg = cfg

        self._update_dictionaries()

        self.cfg["dictionaries_files"] = self.dictionaries_files
        self.cfg.save()
        self.box = QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)

        self.__init_tool()

        self.wizard = wizard.WizardManager(self.cfg)
        self.box.addWidget(self.wizard)
        self.resize(self.cfg["last_width"], self.cfg["minimum_height"])
        # self.setMinimumHeight(self.cfg["minimum_height"])

    def _is_checked_dict(self):
        check_dict = self.config_manager.config_widget.dict_cfg.get_active_dict
        if not check_dict:
            self.show_config_manager()
            self.config_manager.tool.dict_cfg_btn.click()

    def _update_dictionaries(self):
        self.dictionaries_files = serv.get_dictionaries_files(
            self.cfg.dictionaries_dir,
            self.cfg.dictionary_ext)

        files = serv.get_files_by_names(self.cfg.dictionaries_dir,
                                        self.cfg["works_dictionaries"],
                                        self.cfg.dictionary_ext)

        self.work_dictionary = serv.files_to_list(files)

    def __init_tool(self):
        self.tool = tool.Tool(self.cfg)
        self.box.addWidget(self.tool)

        if self.cfg.line_validator:
            self.tool.set_line_validator(self.cfg.line_validator_reg)

    def set_config_manager(self, manager):
        self.config_manager = manager
        self._is_checked_dict()
        self.config_manager.closeEvent = self.config_close_event

    def show_config_manager(self):

        self.config_manager.show()


    def set_controller(self, controller):
        self.controller = controller

    def register_controllers(self):
        if self.controller is not None:
            self.tool.search_btn.clicked.connect(self.controller.enter)
            self.tool.config_btn.clicked.connect(self.controller.open_config)
            self.tool.word_line.returnPressed.connect(
                self.controller.enter)
        else:
            print("controller not installed")

    def set_work_list(self):
        self.work_dictionary = serv.files_to_list(
            serv.get_dictionaries_files(self.cfg.dictionaries_dir,
                                        self.cfg.dictionary_ext))

    def set_omo_words(self):
        work_dictionary = self.work_dictionary
        diff_word = self.tool.line_edit_text
        min_ratio = self.cfg.min_ratio
        prefix_weight = self.cfg.prefix_weight
        max_words = self.cfg.max_words
        words_on_page = self.cfg.words_on_page
        number_columns = self.cfg.number_columns
        search_algorithm = self.cfg.search_algorithm

        if diff_word:

            omo_list = getattr(_diff, search_algorithm)(lst=work_dictionary,
                                                        word=diff_word,
                                                        ratio=min_ratio,
                                                        prefix_weight=prefix_weight)
            if omo_list:
                sorted_on_ratio = _diff.sorted_on_ratio(omo_list)
                cut_omo_list = sorted_on_ratio[:max_words]




                self.wizard.create_pages(max_words, words_on_page)
                self.wizard.set_data(cut_omo_list)
                self.wizard.sort_by(sorter.lexic)
                self.wizard.group_by(serv.group_on_count, words_on_page // number_columns)
                self.wizard.update_table()
                # width = (
                #             self.wizard.wizard.max_column_size + 3) * number_columns
                # height = (self.wizard.wizard.max_line_size + 0) * (
                #     words_on_page // number_columns) + self.cfg[
                #              "tool_height"] + 1
                #
                # if height != self.height():
                #     self.setFixedHeight(height)
                #
                # if width > self.width():
                #     self.resize(width, height)
                #     self.setMinimumWidth(width)
            elif self.wizard.wizard is not None:
                self.wizard.wizard.clear_table()

    def closeEvent(self, *args, **kwargs):
        self.cfg["minimum_height"] = self.height()
        self.cfg["last_width"] = self.width()
        self.cfg.save()

    def config_close_event(self, e):
        all_words = self.config_manager.config_widget.table_cfg.all_words.value()
        words_on_page = self.config_manager.config_widget.table_cfg.words_on_page.value()
        columns = self.config_manager.config_widget.table_cfg.columns.value()

        self.cfg["max_words"] = all_words
        self.cfg["words_on_page"] = words_on_page
        self.cfg["number_columns"] = columns
        self.cfg[
            "search_algorithm"] = self.config_manager.config_widget.search_cfg.algorithm_box.get_active_algorithm()
        self.cfg["works_dictionaries"] = [x.text() for x in
                                          self.config_manager.config_widget.dict_cfg.get_active_dict]
        self._update_dictionaries()
        self.cfg.save()


if __name__ == '__main__':
    from notetub.config import Config

    app = QApplication(sys.argv)
    cfg = Config("path")

    main = MainWindow(cfg=cfg)
    controller = Controller(main)
    main.set_controller(controller)
    main.register_controllers()
    main.show()
    sys.exit(app.exec_())

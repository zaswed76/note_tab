import sys

from PyQt5.QtWidgets import QFrame, QApplication, QVBoxLayout, QMessageBox
from PyQt5.QtCore import *

from notetub.gui import wizard, tool
from notetub.lib import serv, sorter
from notetub.morphlibs import _diff
from notetub.lib import wordpigment


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
        self._work_dictionary_list = None

        self._update_dictionaries()

        self.cfg.save()
        self.box = QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)

        self.__init_tool()
        # self.tool.word_line.setFocus(True)

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
        """

        """

        # пути к файлам согласно списка dict_names
        files = serv.get_files_by_names(self.cfg.dictionaries_dir,
                                        self.cfg["works_dictionaries"],
                                        self.cfg.dictionary_ext)
        # список слов из списка  files если пути существуют

        self._work_dictionary_list, error = serv.files_to_list(files)
        # сохраняем в cfg пути к словарям в директории
        self.cfg["dictionaries_files"] = serv.get_dictionaries_files(
            self.cfg.dictionaries_dir,
            self.cfg.dictionary_ext)

    @property
    def work_dictionary_list(self):
        return self._work_dictionary_list

    def __init_tool(self):
        self.tool = tool.Tool(self.cfg)
        self.box.addWidget(self.tool)

        # if self.cfg.line_validator:
        #     self.tool.set_line_validator(self.cfg.line_validator_reg)

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

        else:
            print("controller not installed")


    @property
    def pigment_word(self):
        """

        :return: выделенные текст в строке ввода
        """
        select_text = self.tool.selected_text()
        if select_text:
            s = select_text
        else:
            s = self.tool.line_edit_text
        return s

    def set_omo_words(self):

        diff_word = self.tool.line_edit_text
        min_ratio = self.cfg.min_ratio
        prefix_weight = self.cfg.prefix_weight
        max_words = self.cfg.max_words
        words_on_page = self.cfg.words_on_page
        number_columns = self.cfg.number_columns
        search_algorithm = self.cfg.search_algorithm

        if diff_word:
            omo_list = getattr(_diff, search_algorithm)(lst=self.work_dictionary_list,
                                                        word=diff_word,
                                                        ratio=min_ratio,
                                                        prefix_weight=prefix_weight)

            if omo_list:
                sorted_on_ratio = _diff.sorted_on_ratio(omo_list)
                # print(sorted_on_ratio)
                print("****************************")
                cut_omo_list = sorted_on_ratio[:max_words]


                self.wizard.create_pages(max_words, words_on_page)
                self.wizard.set_data(cut_omo_list)



                self.wizard.group_by(serv.group_on_count, words_on_page // number_columns)

                # слово выделено - True
                word_selected_flag = self.tool.selected_text()

                pigment = wordpigment.Pigment(self.pigment_word, self.cfg["text_label"],
                                              nsymbol=self.cfg["ndigits"], selected=word_selected_flag)

                self.wizard.set_pigment(pigment)

                self.wizard.update_table()

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
        jaro_prefix = self.config_manager.config_widget.search_cfg.algorithm_options.slider.prefix()


        base_font_family = self.config_manager.config_widget.view_cfg.base_font.font_family
        base_font_size = self.config_manager.config_widget.view_cfg.base_font.font_size
        base_font_color = self.config_manager.config_widget.view_cfg.base_font.color

        pigment_font_family = self.config_manager.config_widget.view_cfg.backlight_font.font_family
        pigment_font_size = self.config_manager.config_widget.view_cfg.backlight_font.font_size
        pigment_font_color = self.config_manager.config_widget.view_cfg.backlight_font.color

        list_border_style = self.config_manager.config_widget.view_cfg.table_app.border_style.current_text()
        border_width = self.config_manager.config_widget.view_cfg.table_app.border_width.value()

        border_color = self.config_manager.config_widget.view_cfg.table_app.border_color
        bg_color = self.config_manager.config_widget.view_cfg.table_app.bg_color



        ndigits = self.config_manager.config_widget.lighting_cfg.nsymb.value()

        self.cfg["list_app"]["list_border_color"] = border_color
        self.cfg["list_app"]["list_bg_color"] = bg_color

        self.cfg["list_app"]["list_border_style"] = list_border_style
        self.cfg["list_app"]["list_border_width"] = border_width
        self.cfg["ndigits"] = ndigits
        self.cfg["text_label"]["base"]["font_family"] = base_font_family
        self.cfg["text_label"]["base"]["font_size"] = base_font_size
        self.cfg["text_label"]["base"]["color"] = base_font_color

        self.cfg["text_label"]["pigment"]["font_family"] = pigment_font_family
        self.cfg["text_label"]["pigment"]["font_size"] = pigment_font_size
        self.cfg["text_label"]["pigment"]["color"] = pigment_font_color

        self.cfg["max_words"] = all_words
        self.cfg["prefix_weight"] = jaro_prefix
        self.cfg["words_on_page"] = words_on_page
        self.cfg["number_columns"] = columns
        self.cfg[
            "search_algorithm"] = self.config_manager.config_widget.search_cfg.algorithm_box.get_active_algorithm()

        self.cfg["works_dictionaries"] = [x.text() for x in
                                          self.config_manager.config_widget.dict_cfg.get_active_dict]

        self._update_dictionaries()
        self.cfg.save()
        # self.tool.set_custom_dict()

    def critical_decode(self, message):
        QMessageBox.critical(self, 'decode', "{}".format(message))



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

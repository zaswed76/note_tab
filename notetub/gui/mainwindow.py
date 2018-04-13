import sys

from PyQt5.QtWidgets import QFrame, QApplication, QVBoxLayout

from notetub.gui import wizard, tool
from notetub.lib import serv
from notetub.morphlibs import _diff


class Controller:
    def __init__(self, parent):
        self.parent = parent

    def enter(self):
        self.parent.set_omo_words()





class MainWindow(QFrame):
    def __init__(self, cfg):
        super().__init__()
        self.controller = None
        self.cfg = cfg
        self.work_dictionary = serv.files_to_list(
            serv.get_dictionaries_files(self.cfg.dictionaries_dir,
                                        self.cfg.dictionary_ext))

        self.resize(500, 500)

        self.box = QVBoxLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.tool = tool.Tool()
        self.box.addWidget(self.tool)

        self.wizard = wizard.WizardManager()
        self.box.addWidget(self.wizard)

    def set_controller(self, controller):
        self.controller = controller

    def register_controllers(self):
        if self.controller is not None:
            self.tool.btn.clicked.connect(self.controller.enter)
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

        if diff_word:
            omo_list = _diff.jaro_winkler(work_dictionary, diff_word, min_ratio,
                                          prefix_weight=prefix_weight)

            sorted_on_ratio = _diff.sorted_on_ratio(omo_list)
            cut_omo_list = sorted_on_ratio[:max_words]

            words = serv.group_by(cut_omo_list, words_on_page//number_columns)

            if words:
                self.wizard.create_pages(max_words, words_on_page)
                self.wizard.set_words(words)
                width = (self.wizard.wizard.max_column_size + 2) * number_columns
                height = (self.wizard.wizard.max_line_size + 2) * (words_on_page // number_columns) + 50

                self.setMinimumSize(width, height)
                self.resize(width, height)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    cfg = Config("path")

    main = MainWindow(cfg=cfg)
    controller = Controller(main)
    main.set_controller(controller)
    main.register_controllers()
    main.show()
    sys.exit(app.exec_())

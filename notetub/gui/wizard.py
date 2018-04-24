from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import *
from notetub.gui import tabwidget, textedit


class WizardManager(QFrame):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.box = QHBoxLayout(self)
        self.box.setContentsMargins(0, 1, 0, 0)
        self.box.setSpacing(0)
        self.wizard = None

    def create_pages(self, max_words, words_on_page):
        if max_words == words_on_page:
            if self.wizard is not None:
                self.box.removeWidget(self.wizard)
            self.wizard = tabwidget.TableList(self.cfg)
            self.box.addWidget(self.wizard)



    def set_words(self, words):
        self.wizard.set_items(words)




class MagicWizard(QWizard):
    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        self.setWizardStyle(QWizard.ClassicStyle)
        buttons_layout = []
        buttons_layout.append(QWizard.Stretch)
        buttons_layout.append(QWizard.NextButton)
        buttons_layout.append(QWizard.BackButton)
        self.setButtonLayout(buttons_layout)
        self.setOption(QWizard.HaveNextButtonOnLastPage)
        self.setOption(QWizard.NoBackButtonOnStartPage)




class Page(QWizardPage):
    def __init__(self, parent):
        super().__init__(parent)
        self.box = QHBoxLayout(self)

    def add_column(self, col):
        self.box.addWidget(col)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())
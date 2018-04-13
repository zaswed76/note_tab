from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtProperty
from PyQt5 import QtCore, QtWidgets


class WizardManager(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

    def set_words(self):
        pass




class MagicWizard(QtWidgets.QWizard):
    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        self.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
        buttons_layout = []
        buttons_layout.append(QtWidgets.QWizard.Stretch)
        buttons_layout.append(QtWidgets.QWizard.NextButton)
        buttons_layout.append(QtWidgets.QWizard.BackButton)
        self.setButtonLayout(buttons_layout)
        self.setOption(QtWidgets.QWizard.HaveNextButtonOnLastPage)
        self.setOption(QtWidgets.QWizard.NoBackButtonOnStartPage)




class Page(QtWidgets.QWizardPage):
    def __init__(self, parent):
        super().__init__(parent)
        self.box = QtWidgets.QHBoxLayout(self)

    def add_column(self, col):
        self.box.addWidget(col)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())
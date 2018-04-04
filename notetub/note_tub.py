from notetub.gui import mainwindow
import sys
from PyQt5.QtWidgets import QApplication

import os
ROOT = os.path.join(os.path.dirname(__file__))
CSS_STYLE = os.path.join(ROOT, "css/style.css")

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(open(CSS_STYLE, "r").read())
    note = mainwindow.MainWindow()
    note.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()





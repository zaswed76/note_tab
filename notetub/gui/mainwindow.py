import sys
from PyQt5.QtWidgets import QFrame, QApplication

class MainWindow(QFrame):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
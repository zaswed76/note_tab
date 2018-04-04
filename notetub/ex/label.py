
import sys
from PyQt5.QtWidgets import QLabel, QApplication, QTextEdit, QFrame, QHBoxLayout
from PyQt5.QtCore import Qt

import os
ROOT = os.path.join(os.path.dirname(__file__))
CSS_STYLE = os.path.join(ROOT, "css/style.css")


class ColumnLabel(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignTop | Qt.AlignTop)


class TabFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.resize(600, 450)
        self.box = QHBoxLayout(self)
        self.columns = []

    def create_columns(self, n):
        for i in range(n):
            self.columns.append(ColumnLabel())
            self.box.addWidget(self.columns[i])

    def set_text(self, text_lst):
        self.create_columns(len(text_lst))
        for col, text in zip(self.columns, text_lst):
            col.setText(text)


if __name__ == '__main__':
    import serv
    words = ""
    app = QApplication(sys.argv)
    main = TabFrame()
    app.setStyleSheet(open("../css/style.css", "r").read())


    text = serv.get_text("../resources/words.txt", 100, 25)

    # print(text_lst)
    print(text)
    # print(text)
    #
    main.set_text(text)

    main.show()
    # main.create_columns(3)
    sys.exit(app.exec_())

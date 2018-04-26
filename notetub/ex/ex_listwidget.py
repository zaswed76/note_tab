import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QHBoxLayout


class Label(QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setText("""<font color=red>PyQt4</font>.</h2>""")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()



    list = QListWidget()


    item_widget = Label()

    list.setItemWidget(QListWidgetItem(list), item_widget)
    window_layout = QVBoxLayout(window)
    window_layout.addWidget(list)
    window.setLayout(window_layout)
    window.show()

    sys.exit(app.exec_())
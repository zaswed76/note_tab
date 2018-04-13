
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.listA = QListWidget(self)
        self.listB = QListWidget(self)
        self.listC = QListWidget(self)

        widgets=[self.listA, self.listB, self.listC]
        layout = QHBoxLayout(self)

        for w1 in widgets:
            layout.addWidget(w1)
            for index in range(100):
                w1.addItem('This is line number %d' % (index +1))
            for w2 in widgets:
                if w1 != w2:
                    w1.verticalScrollBar().valueChanged.connect(w2.verticalScrollBar().setValue)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
#!/usr/bin/env python

from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QPainter)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Text(QGraphicsTextItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFlags(QGraphicsItem.ItemIsSelectable)
        font=QFont()
        font.setPixelSize(20)
        font.setFamily("Helvetica Neue")
        self.setFont(font)
        self.setFrameShape(QFrame.NoFrame)

class Scene(QGraphicsScene):
    def __init__(self, parent, rect):
        super().__init__()
        self.setSceneRect(rect)



class MainWindow(QGraphicsView):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.symbols = []
        self.posx = 0
        self.posy = 0
        self.interval = 10
        self.last_w = 0
        self.setDragMode(QGraphicsView.RubberBandDrag)

        self.scene = Scene(self, QRectF(0, 0, 200, 35))
        self.scene.selectionChanged.connect(self.selected)


        self.setScene(self.scene)
        self.setFixedSize(202, 37)


    def selected(self):
        print([x.toPlainText() for x in self.scene.selectedItems()])

    def set_symbol(self, symbol):

        self.symbols.append(symbol)
        item = Text(symbol)
        w = item.sceneBoundingRect().width()

        self.posx = self.posx + self.last_w -7
        self.last_w = w
        item.setPos(self.posx, self.posy)
        self.scene.addItem(item)

    def keyPressEvent(self, event):
        self.set_symbol(event.text())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec_())
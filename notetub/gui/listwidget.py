import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CustomLabel(QLabel):
    def __init__(self, text, ratio, ratio_in_text=True, ndigits=3,
                 tool_tip=False, lb_font=None, *__args):
        super().__init__(*__args)
        ratio = str(round(ratio, ndigits))
        if ratio_in_text:
            text = "{} {}".format(text, ratio)
        elif tool_tip:
            self.setToolTip(ratio)
        self.setText(text)
        self.select_flag = False

        if lb_font is not None:
            self.setStyleSheet("QLabel {{color: {}}}".format(lb_font["color"]))
            font = QFont()
            font.setFamily(lb_font["font_family"])
            font.setPointSize(int(lb_font["font_size"]))
            self.setFont(font)


    def mousePressEvent(self, QMouseEvent):
        self.select_flag = not self.select_flag
        if self.select_flag:
            self.setStyleSheet("QLabel {color: #51D731;}")
        else:
            self.setStyleSheet("QLabel {color: #636363;}")



class ListWidget(QListWidget):
    def __init__(self, cfg, lb_font):
        super().__init__()
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionRectVisible(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cfg = cfg
        self.lb_font = lb_font
        self.setStyleSheet("""QListWidget
         {{background-color:{list_bg_color};
           border-left: 
             {list_border_width}px
             {list_border_style}
             {list_border_color};
           border-right:  none;
           border-bottom:  none;
           border-top: none;

        }}""".format(**cfg["list_app"]))


    def set_items(self, items):
        ratio_in_text = self.cfg["ratio_in_text"]
        ndigits = self.cfg["ndigits"]
        tool_tip = self.cfg["tool_tip"]

        self.clear()
        for i, r in items:




            item = CustomLabel(i, r, ratio_in_text=ratio_in_text,
                               ndigits=ndigits,
                               tool_tip=tool_tip, lb_font=self.lb_font)
            sitem = QListWidgetItem(self)
            sitem.setSizeHint(item.sizeHint())

            self.setItemWidget(sitem, item)


if __name__ == "__main__":
    from notetub.lib import serv

    app = QApplication(sys.argv)

    model = ListModel()
    mw = ListView()
    mw.setModel(model)

    app.setStyleSheet(open("../css/style.css", "r").read())

    words = serv.group_by(serv.get_words("../resources/words.txt"), 10)
    print(words[0])
    model.set_items(words[0])
    model.set_items(words[0])

    mw.show()
    sys.exit(app.exec())


import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *





class Pigment:
    def __init__(self, pline, pfont):

        self.base_font = pfont["base"]

        self.pigment_font = pfont["pigment"]
        self.pline = pline
        if pline:
            self.pat = re.compile("({})".format(pline))
        else:
            self.pat = None

    def split(self, word):

        if self.pat is not None:
            return re.split(self.pat, word, 1)
        else:
            return word


    def pigment_line(self, ln, font):

        html_line = """style="font-family:'Arial';font-size:25px;color:red">кар"""
        s = """<span style="font-family: 'Helvetica';font-size:20px;color:#636363">тошка</span>"""
        return '<span style="font-size:{font_size}px; color:{color}; font-family:{font_family}">{line}</span>'.format(
            line=ln, **font)
        # return html_line

    def get_pigment(self, line):

        spl = self.split(line)
        if len(spl) == 3:
            pline = self.pigment_line(spl[1], self.pigment_font)
            pre = self.pigment_line(spl[0], self.base_font)

            post = self.pigment_line(spl[2], self.base_font)

            if line == "скарб":
                print(pre)
                print(pline)
                print(post)


            return "<p>{}{}{}</p>".format(pre, pline, post)
        else:
            return self.pigment_line(line, self.base_font)







if __name__ == '__main__':
    font = {'base': {'color': '#636363', 'font_family': 'Helvetica Neue', 'font_size': 20},
            'pigment': {'color': '#1C9C3F', 'font_family': 'Helvetica Neue', 'font_size': 42}}
    pgm = Pigment("кар", font)
    pgm.get_pigment("картошка")

    # class Widget(QLabel):
    #     def __init__(self):
    #         super().__init__()
    #         self.resize(500, 500)
    #
    # app = QApplication(sys.argv)
    # # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    # main = Widget()
    #
    # font = dict(color='green',
    #             font_family='Helvetica Neue',
    #             font_size=12)
    #
    # pgm = Pigment("ров", font)
    # txt = pgm.get_pigment("корова")
    # main.setText(txt)
    # main.show()
    # sys.exit(app.exec_())



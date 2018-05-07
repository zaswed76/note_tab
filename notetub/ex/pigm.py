import re

pline = "ров"
word = "кровать"


class Pigment:
    def __init__(self, pline, pfont):
        self.pfont = pfont
        self.pline = pline
        self.pat = re.compile("({})".format(pline))

    def split(self, word):
        return re.split(self.pat, word, 1)


    def pigment_line(self, ln):
        return '<font size={font_size} color={color} face={font_family}>{line}</font>'.format(
            line=ln, **self.pfont)

    def get_pigment(self, line):
        spl = self.split(line)
        if len(spl) == 3:
            pline = self.pigment_line(spl[1])
            return "<p>{}{}{}</p>".format(spl[0], pline, spl[2])
        else:
            return None


if __name__ == '__main__':
    pass

    font = dict(color='#636363',
                font_family='Helvetica Neue',
                font_size=12)

    pgm = Pigment("ров", font)
    print(pgm.get_pigment("кров"))


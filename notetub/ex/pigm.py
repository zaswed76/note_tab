import re

pline = "ров"
word = "кровать"



def split(word, pline):
    r = re.split(pat, word, 1)
    r.insert(1, pline)
    return r


def font_pigment(line, font):
    return '<font size={font_size} color={color} face={font_family}>{line}</font>'.format(
        line=line, **font)



def line_join(line, font):
    return

def result(line, pat, font):
    pat = re.compile(pline)
    spl = split(line, pat)
    pigm_font = font_pigment(spl[1], font)
    return '<p>{}{}{}</p>'.format(spl[0], pigm_font, spl[2])


font = dict(color= '#636363',
       font_family= 'Helvetica Neue',
       font_size= 12)

pline = "рsв"
pt = re.compile(pline)
print(split("корова", pt))

from os.path import join as pjoin
from notetub.morphlibs.word_item import WordItem

import Levenshtein as lv


def sorted_on_ratio(iterable, reverse=True):
    return sorted(iterable, key=lambda w: w[1], reverse=reverse)
    # print(r)
    # return [x[0] for x in r]


def file_to_words(file):
    """
    получить список слов из файла
    :param file: path
    :return: дшые
    """
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f]


diff_functions = dict(
    jaro_winkler=lv.jaro_winkler,
    jaro=lv.jaro,
    ratio=lv.ratio
)


def test():
    res = []
    for i in range(200000):
        r = lv._levenshtein.jaro_winkler("трава", "дрова", 0.01)
        res.append(r)
    return res[0]


def jaro_winkler(**kwargs):
    """

    :param kwargs:
    :return: список кортежей [(str, float), (слово, рейтинг)]
    """
    lst = kwargs["lst"]
    word = kwargs["word"]
    ratio = kwargs["ratio"]
    prefix_weight = kwargs["prefix_weight"]

    result = []
    result2 = []
    ratio = float(ratio) / 100

    for line in lst:
        r = lv._levenshtein.jaro_winkler(word, line, prefix_weight)

        if r > ratio:
            # print(r)

            # result.append((line, r))
            result2.append(WordItem(line, r))
    return result2

def jaro(**kwargs):
    lst = kwargs["lst"]
    word = kwargs["word"]
    ratio = kwargs["ratio"]
    result = []
    ratio = float(ratio) / 100
    for line in lst:
        r = lv._levenshtein.jaro(word, line)
        if r > ratio:
            result.append((line, r))
    return result

def ratio(**kwargs):
    lst = kwargs["lst"]
    word = kwargs["word"]
    ratio = kwargs["ratio"]
    result = []
    ratio = float(ratio) / 100
    for line in lst:
        r = lv._levenshtein.ratio(word, line)
        if r > ratio:
            result.append((line, r))
    return result

def find(lst, *words):
    d = {}
    for w in words:
        try:
            i = lst.index(w)
        except ValueError:
            print("{} not".format(w))
        else:
            d[w] = i
    return d

def find2(seq, word):
    for n, (w, r) in enumerate(seq):
        # print(item)
        if w == word:
            return "{}, {}, {}".format(n, w, r)
    else:
        return "не найдено"


if __name__ == '__main__':
    # print(test())
    opcorpora_noun_file = pjoin(r"E:\1_SYNS_ORIGINAL\0SYNC\Serg\note_tab\notetub\dictionaries\corpora_noun.txt")
    corp = file_to_words(opcorpora_noun_file)

    dct = dict(lst=corp, word="карофа",  ratio=40, prefix_weight=0.2)
    r = sorted_on_ratio(jaro_winkler(**dct))[:1500]
    r2 = sorted_on_ratio(jaro(**dct))[:1500]
    r3 = sorted_on_ratio(ratio(**dct))[:1500]
    # r = jaro(corp, "ден!м!",  65)
    print(find2(r, "корова"))
    print(find2(r2, "корова"))
    print(find2(r3, "корова"))


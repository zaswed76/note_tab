from os.path import join as pjoin

import Levenshtein as lv


def sorted_on_ratio(iterable, reverse=True):
    r = sorted(iterable, key=lambda w: w[1], reverse=reverse)
    return [x[0] for x in r]


def file_to_words(file):
    """
    получить список слов из файла
    :param file: path
    :return: дшые
    """
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f]


diff_functions = dict(
    distance=lv.distance,
    jaro_winkler=lv.jaro_winkler,
    jaro=lv.jaro_winkler,
    ratio=lv.ratio
)


def test():
    res = []
    for i in range(200000):
        r = lv._levenshtein.jaro_winkler("трава", "дрова", 0.01)
        res.append(r)
    return res[0]


def jaro_winkler(lst, word, ratio, prefix_weight=0.1):
    result = []
    ratio = float(ratio) / 100
    for line in lst:
        r = lv._levenshtein.jaro_winkler(word, line, prefix_weight)
        if r > ratio:
            result.append((line, r))
    return result

def jaro(lst, word, ratio):
    result = []
    ratio = float(ratio) / 100
    for line in lst:
        r = lv._levenshtein.jaro(word, line)
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


if __name__ == '__main__':
    # print(test())
    opcorpora_noun_file = pjoin("../resource/dictionaries/corpora_noun.txt")
    corp = file_to_words(opcorpora_noun_file)

    r = jaro_winkler(corp, "потрит",  40, prefix_weight=0.01)
    # r = jaro(corp, "ден!м!",  65)
    print(sorted_on_ratio(r)[:1550])
    print(find(sorted_on_ratio(r)[:1550], "портрет", "патриот"))

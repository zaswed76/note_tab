
import pprint
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
    distance=lambda w, line: lv.distance(w, line),
    jaro_winkler=lambda w, line, pr: lv.jaro_winkler(w, line, pr),
    jaro=lambda w, line: lv.jaro_winkler(w, line),
    ratio=lambda w, line: lv.ratio(w, line)
)

def diff(fun, lst, word, ratio, *prefix):
    result = []
    ratio = float(ratio)/100

    for line in lst:

        r = lv.jaro_winkler(word, line, 0.2)

        if r > ratio:
            result.append((line, r))
    return result






if __name__ == '__main__':
    import numpy as np

    opcorpora_noun_words = r"D:\0SYNC\python_projects\cube_projects\libs\rumorph\rumorph\resources\NOUNS\corpora_noun.txt"
    corp = file_to_words(opcorpora_noun_words)
    rvc = corp

    r = diff(diff_functions['jaro_winkler'], rvc, "птрет", 80)
    print(sorted_on_ratio(r))
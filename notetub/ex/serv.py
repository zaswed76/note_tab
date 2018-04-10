import pprint
from itertools import groupby

import math


def get_words(file, nword=0):
    with open(file, "r", encoding="utf-8") as f:
        word_lst = [x.strip() for x in f.readlines()]
        if nword:
            n = nword
        else:
            n = len(word_lst)
        cut_lst = word_lst[:n]
        return cut_lst

def group_by(lst, by=None):
    """ Группировка элементов последовательности по count элементов """
    return [lst[i:i+by] for i in range(0,len(lst),by)]


def text_lst(lst):
    r = []
    for wlst in lst:
        r.append("\n".join(wlst))
    return r


def get_text(file, nword=0, ncol=1):
    lst = get_words(file, nword)
    group_lst = group_by(lst, ncol)
    return text_lst(group_lst)

def group_on_lst(lst, words_on_page, number_columns):
    r = []
    nwords = words_on_page//number_columns
    print(nwords)
    pages = group_by(lst, words_on_page)
    for p in pages:

        r.append(group_by(p, nwords))
    return r

def chunks(seq, num):
  return groupby(int(math.ceil(len(seq) / float(num))), seq)


def split(lst, n):
    r = group_by(lst, len(lst)//n)
    if len(r) > n:
        ost = r.pop()
        for i, e in enumerate(ost):
            sorted(r, reverse=True)[i].append(e)
        return r

    else:
        return r


if __name__ == '__main__':
    l = list(range(12))

    print(split(l, 5))
    # print(group_by(lst, 4))
    # split_list = lambda n: zip(*[iter(l+[None]*((n-len(l)%n)%n))]*n)
    # print(list(split_list(4)))
    # pprint.pprint(group_on_lst(lst, 10, 3))

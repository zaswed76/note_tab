import fileinput
import glob
from os.path import join as pjoin
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




def text_lst(lst):
    r = []
    for wlst in lst:
        r.append("\n".join(wlst))
    return r


def get_text(file, nword=0, ncol=1):
    lst = get_words(file, nword)
    group_lst = group_by(lst, ncol)
    return text_lst(group_lst)



def group_by(lst, by=None):
    """ Группировка элементов последовательности по count элементов """
    return [lst[i:i+by] for i in range(0,len(lst),by)]

def group_on_lst(lst, words_on_page, number_columns):
    r = []
    nwords = words_on_page//number_columns
    pages = group_by(lst, words_on_page)
    for p in pages:

        r.append(chunks(p, nwords))
    return r

def chunks(items, chunks_quantity):
    chunk_len = len(items) // chunks_quantity
    rest_count = len(items) % chunks_quantity
    chunks = []
    for i in range(chunks_quantity):
        chunk = items[:chunk_len]
        items = items[chunk_len:]
        if rest_count and items:
            chunk.append(items.pop(0))
            rest_count -= 1

        chunks.append(chunk)

    return chunks

def file_to_list(file):
    """
    получить список слов из файла
    :param file: path
    :return: дшые
    """
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f]

def files_to_list(files):
    s = set()
    for f in files:
        s.update(set(file_to_list(f)))
    return sorted(s)


def get_dictionaries_files(folder, ext):
    return glob.glob(pjoin(folder, '*' + ext))




if __name__ == '__main__':
    files = get_dictionaries_files("../resource/test", ".txt")
    print(files_to_list(files))

    # print(group_by(lst, 4))
    # split_list = lambda n: zip(*[iter(l+[None]*((n-len(l)%n)%n))]*n)
    # print(list(split_list(4)))
    # pprint.pprint(group_on_lst(lst, 10, 3))

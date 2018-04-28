import fileinput
import glob
import os
from os import path
import shutil

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



def group_on_count(lst, by=None):
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
    error = None
    with open(file, "r", encoding="utf-8") as f:
        try:
            r = [x.strip() for x in f]
        except UnicodeDecodeError as mes:
            r = []
            error = mes
        return r, error

def files_to_list(files: list):
    """

    :param files: list < str
    :return: список слов из файлов указанных в list files
    """
    s = set()
    error = None
    for f in files:
        if os.path.isfile(f):
            lst, error = file_to_list(f)
            if lst:
                lst[0] = lst[0].replace("\ufeff", "")
            s.update(set(lst))
    return sorted(s), error


def get_dictionaries_files(folder, ext):
    """

    :param folder: str
    :param ext: str
    :return: list < str словари в указанной директории
    """
    return glob.glob(path.join(folder, '*' + ext))

def get_files_by_names(folder, dict_names, ext):
    """

    :param folder: str
    :param dict_names: list < str
    :param ext: str
    :return: пути к файлам согласно списка dict_names
    """
    fd = []
    for n in dict_names:
        fd.append(path.join(folder, n + ext))
    return fd



def add_dict(dpath, dict_dir, ext):
    if path.isfile(dpath):
        if path.splitext(dpath)[1] == ext:
            base_name = path.basename(dpath)
            target = path.join(dict_dir, base_name)
            shutil.copy2(dpath, target)
            return path.splitext(base_name)[0]


def del_dict(del_item, directory, ext):
    print(del_item)
    pth = path.join(directory, del_item+ext)
    if os.path.isfile(pth):
        os.remove(pth)
        return pth

if __name__ == '__main__':
    files = get_dictionaries_files("../dictionaries", ".txt")
    print(files_to_list(files))

    # print(group_by(lst, 4))
    # split_list = lambda n: zip(*[iter(l+[None]*((n-len(l)%n)%n))]*n)
    # print(list(split_list(4)))
    # pprint.pprint(group_on_lst(lst, 10, 3))



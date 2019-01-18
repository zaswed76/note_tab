
import os
import pickle
import _pickle as cPickle

from omo_objects import paths
from omo_objects.word.word_item import WordItem

db_path = os.path.join(paths.ROOT, "dictionaries", "corpora_noun.pcl")
dictionary_path = os.path.join(paths.ROOT, "dictionaries", "corpora_noun.txt")



def file_to_words(file):
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f]

def save_obj(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(path):
    with open(path, 'rb') as f:
        return cPickle.load(f)



if __name__ == '__main__':

    # lst_words = file_to_words(dictionary_path)
    #
    # d = {}
    # for w in lst_words:
    #     d[w] = WordItem(w)
    #
    # save_obj(d, db_path)

    print(load_obj(db_path))









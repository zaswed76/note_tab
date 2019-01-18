import pickle

vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
vowels_line = "".join(vowels)
trantab_cyrillic_vowels = str.maketrans("", "", vowels_line)
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к',
              'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

deaf_ring_id = str.maketrans("бпвфгкдтжшзс", "112233445566")

def replace_characters(line, trantab):
    """

    :param trantab: str.maketrans
    :param line: str cirillisa
    :return: new line str
    """
    return line.translate(trantab)

class LetterObject:
    def __init__(self, let):
        self.let = let

d = {}
alt_dct = {k: v for k, v in zip("бвгджз", "пфктшс")}
alt_dct2 = {k: v for k, v in zip("пфктшс", "бвгджз")}
alt_dct.update(alt_dct2)



class WordItem:
    def __init__(self, word, lev_ratio=None):
        self.word = word
        self.lev_ratio = lev_ratio
        self.cons_skeleton = replace_characters(self.word, trantab_cyrillic_vowels)
        self.cons_deaf_ring_id = replace_characters(self.cons_skeleton, deaf_ring_id)

    @staticmethod
    def compare(word1, word2):
        # print("{} == {}".format(word1.cons_skeleton, word2.cons_skeleton))
        r = 0
        for n, (lw, fw) in enumerate(zip(word1.cons_skeleton, word2.cons_skeleton), start=1):
            # print(lw, fw)
            if lw == fw:
                r += 30/n
            elif lw == alt_dct.get(fw):
                r += 20/n
            else:
                pass
        return r/100 - 0.28

    def __repr__(self):
        return "({})".format(self.word)

def file_to_words(file):
    """
    получить список слов из файла
    :param file: path
    :return: дшые
    """
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f]

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

if __name__ == '__main__':
    # word_line = WordItem("пово")
    # find_word1 = WordItem("пво", 0.75)
    # from os.path import join as pjoin
    # import pickle
    # opcorpora_noun_file = pjoin(r"E:\1_SYNS_ORIGINAL\0SYNC\Serg\note_tab\notetub\dictionaries\corpora_noun.txt")
    # corp = file_to_words(opcorpora_noun_file)
    #
    # print(corp)
    #
    # d = {}
    # for w in corp:
    #     d[w] = WordItem(w)
    #
    # save_obj(d, "corp_word_items")

    word_line = WordItem("карова")
    d = load_obj("corp_word_items")
    print(d["корова"].cons_skeleton)
    for kw, wi in d.items():
        r = WordItem.compare(wi, word_line)
        if r >= 0.20:
            print(wi, wi.cons_skeleton, r)

    #
    # print(word_line.compare(find_word1))


    # print(replace_characters("крф", test_trantab))
    # print(replace_characters("крв", test_trantab))
    # print(replace_characters("короб", test_trantab))

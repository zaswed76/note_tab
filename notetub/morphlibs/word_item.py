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



    def compare(self, word):
        print("{} == {}".format(self.cons_skeleton, word.cons_skeleton))
        r = 0
        for n, (lw, fw) in enumerate(zip(self.cons_skeleton, word.cons_skeleton), start=1):
            print(lw, fw)
            if lw == fw:
                r += 30/n
            elif lw == alt_dct.get(fw):
                r += 20/n
            else:
                pass
        return r/100 - 0.28



    def __repr__(self):
        return str(self.word)


if __name__ == '__main__':
    word_line = WordItem("повод")
    find_word1 = WordItem("п", 0.75)

    print(word_line.compare(find_word1))


    # print(replace_characters("крф", test_trantab))
    # print(replace_characters("крв", test_trantab))
    # print(replace_characters("короб", test_trantab))

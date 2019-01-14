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


class WordItem:
    def __init__(self, word, lev_ratio=None):
        self.word = word
        self.lev_ratio = lev_ratio
        self.cons_skeleton = replace_characters(self.word, trantab_cyrillic_vowels)
        self.cons_deaf_ring_id = replace_characters(self.cons_skeleton, deaf_ring_id)



    def compare(self, word):
        print("{} == {}".format(self.word, word))

    def __repr__(self):
        return str(self.word)


if __name__ == '__main__':
    word = "корова"
    it = ("корова", 0.25)
    wi = WordItem(*it)
    print(wi.cons_skeleton)
    print(wi.cons_deaf_ring_id)

    # print(replace_characters("крф", test_trantab))
    # print(replace_characters("крв", test_trantab))
    # print(replace_characters("короб", test_trantab))

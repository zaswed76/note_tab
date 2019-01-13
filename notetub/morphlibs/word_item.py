vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
vowels_line = "".join(vowels)
trantab_cyrillic_vowels = str.maketrans("", "", vowels_line)
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к',
              'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']


def consonants_skeleton(line, trantab):
    """

    :param trantab: str.maketrans
    :param line: str cirillisa
    :return: new line str
    """
    return line.translate(trantab)


class WordItem:
    def __init__(self, word_item):
        self.word_item = word_item
        self.word = word_item[0]
        self.ratio = word_item[1]

    def compare(self, word):
        print("{} == {}".format(self.word, word))

    def __repr__(self):
        return str(self.word_item)


if __name__ == '__main__':
    word = "корал"
    it = ("карол", 0.25)
    wi = WordItem(it)
    wi.compare(word)

    print(consonants_skeleton(word, trantab_cyrillic_vowels))

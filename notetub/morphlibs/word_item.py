vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к',
              'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']


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

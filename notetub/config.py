class Config:
    def __init__(self, cfg):
        self.cfg = cfg

    @property
    def max_words(self):
        return 50

    @property
    def words_on_page(self):
        return 50
    @property
    def number_columns(self):
        return 5
    @property
    def min_ratio(self):
        return 50
    @property
    def prefix_weight(self):
        return 0.2

    @property
    def dictionaries_dir(self):
        return "./resource/dictionaries"

    @property
    def dictionary_ext(self):
        return ".txt"
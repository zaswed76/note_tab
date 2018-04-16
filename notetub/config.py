import yaml


class Config:
    def __init__(self, pth):
        self.pth = pth
        self._data = {}

    def load_cfg(self):
        with open(self.pth, "r") as f:
            self._data = yaml.load(f)

    def save(self):
        with open(self.pth, "r") as f:
            self._data = yaml.load(f)

    @property
    def data(self):
        return self._data

    @property
    def max_words(self):
        return self.data["max_words"]

    @property
    def words_on_page(self):
        return self.data["words_on_page"]

    @property
    def number_columns(self):
        return self.data["number_columns"]

    @property
    def min_ratio(self):
        return self.data["min_ratio"]

    @property
    def prefix_weight(self):
        return self.data["prefix_weight"]

    @property
    def dictionaries_dir(self):
        return self.data["dictionaries_dir"]

    @property
    def dictionary_ext(self):
        return self.data["dictionary_ext"]

    @property
    def line_validator_reg(self):
        return self.data["line_validator_reg"]

    @property
    def line_validator(self):
        return self.data["line_validator"]


if __name__ == '__main__':
    pth = "./etc/cfg.yaml"

    cfg = Config(pth)
    cfg.load_cfg()
    print(cfg.data)

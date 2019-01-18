import yaml




from collections.abc import MutableMapping


class Config(MutableMapping):
    def __init__(self, pth):
        self.pth = pth
        self._data = {}

    @property
    def data(self):
        return self._data

    def load_cfg(self):
        with open(self.pth, "r") as f:
            self._data = yaml.load(f)

    def save(self):
        with open(self.pth, "w") as f:
            yaml.dump(self._data, f, default_flow_style=False,
                      allow_unicode=True)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return self._data.__iter__()

    def __contains__(self, key):
        return self._data.__contains__(self, id(key))

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):

        self._data[key] = value


    def __delitem__(self, key):
        del(self._data[key])

    def __str__(self):
        return str(self._data)

    def __getattr__(self, attr):
        return self._data[attr]

    # def __setattr__(self, key, value):
    #     print(self._data, 111)
    #     print("----------------")
    #     self._data.__setattr__(self, key, value)
    #
    #     print(self._data, 222)

if __name__ == '__main__':
    pth = "./etc/cfg.yaml"

    cfg = Config(pth)
    cfg.load_cfg()
    print(cfg.data)
    cfg.line_validator["line_validator"] = 5
    print(cfg.data)

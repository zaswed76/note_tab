try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping


class Md(MutableMapping):
    '''A dict that can take mutable objects as keys.'''

    def __init__(self):
        self._data = {}

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

if __name__ == '__main__':
    md = Md()

    md["a"] = 1

    md.a = 7
    print(md.a)
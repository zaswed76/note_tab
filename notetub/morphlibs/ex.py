from collections.abc import MutableSequence

ls1 = [("A", 10), ("B", 20)]
ls2 = [("A", 7), ("C", 8)]


d = {}

class MyList(MutableSequence):
    def __init__(self):
        self._inner_list = []

    def __len__(self):
        return len(self._inner_list)

    def __delitem__(self, index):
        self._inner_list.__delitem__(index - 1)

    def insert(self, index, value):
        self._inner_list.insert(index - 1, value)

    def __setitem__(self, index, value):
        self._inner_list.__setitem__(index - 1, value)

    def __getitem__(self, index):
        return self._inner_list.__getitem__(index - 1)

    def __add__(self, other):
        self._inner_list.extend(other)





for lst in ls1, ls2:
    for it in lst:
        d[it[0]] = d.get(it[0], []) + [it[1]]

nd = dict()
for k, v in d.items():
    nd[k] = sum(v)/len(v)
print(nd)
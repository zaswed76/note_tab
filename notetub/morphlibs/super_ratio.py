from  _diff import jaro_winkler, jaro, ratio, pjoin, file_to_words, sorted_on_ratio

my_diff_functions = {
    'jaro_winkler': jaro_winkler,
    'jaro': jaro,
    'ratio': ratio
}

def mix(seq):
    nd = dict()
    d = dict()
    for lst in seq:
        for it in lst:
            d[it[0]] = d.get(it[0], []) + [it[1]]

    for k, v in d.items():
        nd[k] = sum(v)/len(v)
    return nd

def mix_diff(**kwargs):
    result_lst = []
    for func in my_diff_functions.values():
        result_lst.append(sorted_on_ratio(func(**kwargs)))
    return result_lst



if __name__ == '__main__':
    # print(test())
    opcorpora_noun_file = pjoin(
        r"E:\1_SYNS_ORIGINAL\0SYNC\Serg\note_tab\notetub\dictionaries\corpora_noun.txt")
    corp = file_to_words(opcorpora_noun_file)

    dct = dict(lst=corp, word="карол", ratio=80, prefix_weight=0.2)

    print(mix(mix_diff(**dct)))
    print("--------------")
    resjaro(**dct))
    # r = jaro_winkler(**dct)
    # # r = jaro(corp, "ден!м!",  65)
    # print(sorted_on_ratio(r)[:200])

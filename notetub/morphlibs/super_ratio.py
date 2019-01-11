from  _diff import jaro_winkler, jaro, ratio, pjoin, file_to_words, sorted_on_ratio

my_diff_functions = {
    'jaro_winkler': jaro_winkler,
    'jaro': jaro,
    'ratio': ratio
}


def mix_diff(**kwargs):
    # lst = kwargs["lst"]
    # word = kwargs["word"]
    # ratio = kwargs["ratio"]
    # prefix_weight = kwargs["prefix_weight"]


    result_lst = set()

    for func in my_diff_functions.values():
        print(sorted_on_ratio(func(**kwargs)))
        print("-------------")


if __name__ == '__main__':
    # print(test())
    opcorpora_noun_file = pjoin(
        r"E:\1_SYNS_ORIGINAL\0SYNC\Serg\note_tab\notetub\dictionaries\corpora_noun.txt")
    corp = file_to_words(opcorpora_noun_file)

    dct = dict(lst=corp, word="корол", ratio=90, prefix_weight=0.2)

    mix_diff(**dct)
    # r = jaro_winkler(**dct)
    # # r = jaro(corp, "ден!м!",  65)
    # print(sorted_on_ratio(r)[:200])

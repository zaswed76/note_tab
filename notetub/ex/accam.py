a = [("a", 1), ("b", 2)]



def group(lst):
    words  = []
    ratio = []
    for w, r in lst:
        words.append(w)
        ratio.append(r)
    return words, ratio


print(group(a))
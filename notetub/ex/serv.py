

def get_words(file, nword=0):
    with open(file, "r") as f:
        word_lst = [x.strip() for x in f.readlines()]
        if nword:
            n = nword
        else:
            n = len(word_lst)
        cut_lst = word_lst[:n]
        return cut_lst

def group(lst, siz):
    """ Группировка элементов последовательности по count элементов """
    return [lst[i:i+siz] for i in range(0,len(lst),siz)]


def text_lst(lst):
    r = []
    for wlst in lst:
        r.append("\n".join(wlst))
    return r


def get_text(file, nword=0, ncol=1):
    lst = get_words(file, nword)
    group_lst = group(lst, ncol)
    return text_lst(group_lst)
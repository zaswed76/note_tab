

def lexic(data):
    r =sorted(data, key=lambda w: w[0], reverse=False)
    print(r)
    return r
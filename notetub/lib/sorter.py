

def lexic(data):
    r =sorted(data, key=lambda w: w[1], reverse=True)
    print(r)
    return r
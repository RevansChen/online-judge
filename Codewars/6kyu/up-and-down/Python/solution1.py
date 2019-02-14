# Python - 3.6.0

odd_func = lambda i, j: len(i) < len(j)
even_func = lambda i, j: len(i) > len(j)

def arrange(strng):
    ts = strng.split(' ')
    for i in range(len(ts) - 1):
        comp_func = odd_func if i & 1 else even_func
        if comp_func(ts[i], ts[i + 1]):
            ts[i], ts[i + 1] = ts[i + 1], ts[i]
    for i in range(len(ts)):
        ts[i] = ts[i].upper() if i & 1 else ts[i].lower()
    return ' '.join(ts)

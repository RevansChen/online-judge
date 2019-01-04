# Python - 3.6.0

def two_decimal_places(n):
    sp = str(n).split('.')
    i, p = sp[0], sp[1][0:3]
    if len(p) == 3:
        pt, r = int(p[0:2]), int(p[2])
        pt += 1 if r >= 5 else 0
    return float('%s.%02d' % (i, pt))

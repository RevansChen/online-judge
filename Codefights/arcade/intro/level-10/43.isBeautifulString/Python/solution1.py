# Python3

def isBeautifulString(inputString):
    dc = { c: inputString.count(c) for c in set(inputString) }
    count = dc.get('a', 0)
    for i in range(ord('b'), ord('z') + 1):
        c = chr(i)
        if c in dc:
            if dc[c] > count:
                return False
            count = dc[c]
        else:
            count = 0
    return True

# Python3

def isIPv4Address(inputString):
    from functools import reduce
    addr = inputString.split('.')
    if (len(addr) != 4):
        return False
    if (not reduce(lambda x, y: x and y, [ a.isnumeric() for a in addr ])):
        return False
    return reduce(lambda x, y: x and y, [ (0 <= i) and (i <= 255) for i in map(int, addr) ])

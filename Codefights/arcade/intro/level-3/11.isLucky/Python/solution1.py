# Python3

def isLucky(n):
    n = list(str(n))
    _sum = lambda ls: sum(map(int, ls))
    return _sum(n[:len(n) // 2]) == _sum(n[len(n) // 2:])

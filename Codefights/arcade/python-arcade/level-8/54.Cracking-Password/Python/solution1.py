# Python3

# 有限制修改區域
from itertools import product, filterfalse

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(filterfalse(lambda digs: int(digs) % d, map(createNumber, product(digits, repeat = k))))

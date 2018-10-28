# Python3

# 有限制修改區域
from itertools import count, takewhile

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)

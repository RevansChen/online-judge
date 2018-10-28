# Python3

# 有限制修改區域
from itertools import dropwhile, chain, repeat

def memoryPills(pills):
    gen = chain(dropwhile(lambda s: len(s) & 1, pills), repeat(''))
    next(gen)
    return [next(gen) for _ in range(3)]

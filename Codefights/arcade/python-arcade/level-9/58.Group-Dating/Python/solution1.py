# Python3

# 有限制修改區域
def groupDating(male, female):
    return [*map(list, zip(*[ (e, female[i]) for i, e in enumerate(male) if e != female[i] ]))] or [[], []]

# Python3

import functools

# 有限制修改區域
def fibonacciList(n):
    return [[0] * x for x in functools.reduce(lambda ls, i: ls + [ls[-1] + ls[-2]], range(n - 2), [0, 1])]

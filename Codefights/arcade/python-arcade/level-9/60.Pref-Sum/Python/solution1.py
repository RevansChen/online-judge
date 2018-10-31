# Python3

import functools

# 有限制修改區域
def prefSum(a):
    return functools.reduce(lambda ls, e: ls + [ls[-1] + e], a[1:], [a[0]])

# Python3

import math

# 有限制修改區域
def compose(f, g):
    return lambda x: f(g(x))

def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)

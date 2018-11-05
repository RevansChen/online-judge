# Python3

import functools
import math

# 有限制修改區域
def compose(functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)

def functionsComposition(functions, x):
    return compose(map(eval, functions))(x)


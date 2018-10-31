# Python3

import functools

# 有限制修改區域
def mathPractice(numbers):
    return functools.reduce(lambda x, y: x * y[0] + (y[1] if len(y) == 2 else 0), [ numbers[i:i + 2] for i in range(2, len(numbers), 2)], sum(numbers[:2]))

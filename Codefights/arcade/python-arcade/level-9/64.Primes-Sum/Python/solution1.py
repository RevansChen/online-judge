# Python3

# 有限制修改區域
def primesSum(a, b):
    return sum(i for i in range(a, b + 1) if all(i % j for j in range(min(i, 2), int(i ** 0.5) + 1)))

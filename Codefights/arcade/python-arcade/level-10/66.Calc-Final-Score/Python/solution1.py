# Python3

# 有限制修改區域
def calcFinalScore(scores, n):
    gen = map(lambda x: x * x, sorted(scores, reverse = True))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res

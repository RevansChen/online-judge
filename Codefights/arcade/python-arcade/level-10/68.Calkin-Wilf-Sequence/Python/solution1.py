# Python3

# 有限制修改區域
def calkinWilfSequence(number):
    def fractions():
        a, b = 1, 1
        while True:
            yield [a, b]
            a, b = b, 2 * (a - a % b) + b - a

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res

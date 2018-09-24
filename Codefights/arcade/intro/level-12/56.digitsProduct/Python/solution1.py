# Python3

from functools import reduce

def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1

    digits = []
    n = product
    for i in range(9, 1, -1):
        while n % i == 0:
            digits.append(i)
            n //= i

    if len(digits) == 0 or n != 1:
        return -1

    return reduce(lambda x, y: x * 10 + y, digits[::-1])

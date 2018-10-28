# Python3

# 有限制修改區域
from itertools import permutations

def kthPermutation(numbers, k):
    return [*permutations(numbers)][k - 1]

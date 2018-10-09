# Python3

# 有限制修改區域
def killKthBit(n, k):
    return n & ~(1 << (k - 1))

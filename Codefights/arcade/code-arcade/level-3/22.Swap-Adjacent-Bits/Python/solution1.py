# Python3

# 有限制修改區域
def swapAdjacentBits(n):
    return ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1)

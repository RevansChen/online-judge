# Python3

# 有限制修改區域
def secondRightmostZeroBit(n):
    return 2 ** [i for i, b in enumerate(bin(n)[2:][::-1]) if b == '0'][1]

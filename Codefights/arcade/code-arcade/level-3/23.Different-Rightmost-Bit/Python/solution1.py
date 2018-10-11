# Python3

# 有限制修改區域
def differentRightmostBit(n, m):
    return 2 ** [i for i, b in enumerate(bin(n ^ m)[2:][::-1]) if b == '1'][0]

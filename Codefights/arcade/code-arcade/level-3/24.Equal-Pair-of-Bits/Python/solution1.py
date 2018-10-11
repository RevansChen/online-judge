# Python3

# 有限制修改區域
def equalPairOfBits(n, m):
    return 2 ** [i for i, b in enumerate(bin(n ^ m)[2:].rjust(len(bin(max(n , m))) - 2, '0')[::-1]) if b == '0'][0]

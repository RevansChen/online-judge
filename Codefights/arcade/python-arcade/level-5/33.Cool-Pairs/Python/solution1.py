# Python3

# 有限制修改區域
def coolPairs(a, b):
    uniqueSums = {(i + j) for i in a for j in b if ((i * j) % (i + j)) == 0}
    return len(uniqueSums)

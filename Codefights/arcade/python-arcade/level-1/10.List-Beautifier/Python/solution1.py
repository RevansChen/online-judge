# Python3

# 有限制修改區域
def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        _, *res, _ = res
    return res

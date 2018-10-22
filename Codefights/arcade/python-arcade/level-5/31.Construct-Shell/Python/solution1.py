# Python3

# 有限制修改區域
def constructShell(n):
    return [[0] * (i if i <= n else (2 * n - i)) for i in range(1, 2 * n)]

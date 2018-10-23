# Python3

# 有限制修改區域
def fixResult(result):
    def fix(x):
        return x // 10

    return list(map(fix, result))

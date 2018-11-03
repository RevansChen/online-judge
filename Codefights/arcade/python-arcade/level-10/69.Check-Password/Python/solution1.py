# Python3

# 有限制修改區域
def checkPassword(attempts, password):
    def check():
        while True:
            yield ((yield) == password)

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1

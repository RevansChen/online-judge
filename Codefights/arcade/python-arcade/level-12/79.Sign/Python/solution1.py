# Python3

# 有限制修改區域
class Functions(object):
    @staticmethod
    def sign(x):
        return 1 if x > 0 else (-1 if x else 0)

def sign(x):
    return Functions.sign(x)

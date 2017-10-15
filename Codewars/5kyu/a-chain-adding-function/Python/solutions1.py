# Python - 3.4.3

# 繼承int, 並實作call的特性
class Integer(int):
    def __call__(self, *args, **kwargs):
        return Integer(self + args[0])

# add()函數將回傳一個自製的int類別
def add(val):
    return Integer(val)
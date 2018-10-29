# Python3

# 有限制修改區域
def pressureGauges(morning, evening):
    return [*map(list, zip(*map(lambda x:(min(x), max(x)), zip(morning, evening))))]

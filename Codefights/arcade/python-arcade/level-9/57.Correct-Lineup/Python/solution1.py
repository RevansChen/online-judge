# Python3

# 有限制修改區域
def correctLineup(athletes):
    return [ e for pair in zip(athletes[1::2], athletes[::2]) for e in pair ]

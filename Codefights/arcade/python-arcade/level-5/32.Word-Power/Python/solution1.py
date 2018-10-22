# Python3

# 有限制修改區域
def wordPower(word):
    num = {chr(i + ord('a')): (i + 1) for i in range(26)}
    return sum([num[ch] for ch in word])

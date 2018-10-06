# Python3

def phoneCall(min1, min2_10, min11, s):
    if s < min1:
        return 0
    s -= min1

    duration2_10 = s // min2_10
    if duration2_10 <= 9:
        return 1 + duration2_10
    s -= min(9, duration2_10) * min2_10

    return 10 + s // min11

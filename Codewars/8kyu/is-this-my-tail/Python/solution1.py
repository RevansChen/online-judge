# Python - 2.7.6

def correct_tail(body, tail):
    start = len(body) - len(tail)
    # 起始位置不可為負值, 且body尾端與tail相同
    return start >= 0 and body[start:] == tail
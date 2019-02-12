# Python - 3.6.0

def solution(s, length = 2):
    num = len(s) % length
    if num > 0:
        s += '_' * (length - num)
    return [s[i:i + length] for i in range(0, len(s), length)]

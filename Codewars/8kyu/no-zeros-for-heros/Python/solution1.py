# Python - 3.6.0

def no_boring_zeros(n):
    x = str(n).strip('0')
    return int(x) if x else 0

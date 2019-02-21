# Python - 3.6.0

def last_digit(n1, n2):
    if not n2:
        return 1
    n1 %= 10
    r = 1
    while n2 > 1:
        n2, m = n2 >> 1, n2 & 1
        if m:
            r = (r * n1) % 10
        n1 = (n1 * n1) % 10
    return (n1 * r) % 10

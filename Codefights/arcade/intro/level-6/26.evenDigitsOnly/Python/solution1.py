# Python3

def evenDigitsOnly(n):
    return not bool(sum(1 for d in str(n) if (int(d) % 2)))

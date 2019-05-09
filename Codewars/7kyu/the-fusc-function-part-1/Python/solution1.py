# Python - 3.6.0

fusc = lambda n: n if n <= 1 else (fusc(n >> 1) + ((n & 1) and fusc((n >> 1) + 1)))

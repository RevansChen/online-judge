# Python - 3.6.0

def how_much_water(L, X, N):
    if N > (2 * X):
        return 'Too much clothes'
    elif N < X:
        return 'Not enough clothes'
    else:
        return round(L * (1.1 ** (N - X)), 2)

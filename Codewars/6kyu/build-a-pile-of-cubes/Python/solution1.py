# Python - 3.6.0

def find_nb(m):
    n, sum = 1, 0
    while (m > sum):
        sum += n ** 3
        n += 1
    return n - 1 if m == sum else -1

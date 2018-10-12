# Python3

def leastFactorial(n):
    k = 1
    i = 2
    while k < n:
        k *= i
        i += 1
    return k

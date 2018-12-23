# Python - 3.6.0

def digitize(n):
    lst = []
    while n:
        lst.append(n % 10)
        n //= 10
    return lst

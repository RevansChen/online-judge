# Python - 3.4.3

def hotpo(n):
    times = 0
    while n > 1:
        if (n % 2) == 1:
            n = 3 * n + 1
        else:
            n //= 2
        times += 1
    return times
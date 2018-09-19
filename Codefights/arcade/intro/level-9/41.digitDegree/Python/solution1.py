# Python3

def digitDegree(n):
    times = 0
    while n >= 10:
        times += 1
        val = n
        newN = 0
        while val:
            newN += val % 10
            val //= 10
        n = newN
    return times

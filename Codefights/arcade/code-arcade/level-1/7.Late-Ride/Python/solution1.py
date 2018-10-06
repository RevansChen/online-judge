# Python3

def lateRide(n):
    return sum(map(int, ''.join(map(str, divmod(n, 60)))))

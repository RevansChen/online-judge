# Python - 2.7.6

def isPrime(num):
    if (num == 2):
        return True
    if (num & 1) == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if (num % i) == 0:
            return False
    return True

def prime_bef_aft(num):
    befPrime = num - 1
    aftPrime = num + 1
    while not isPrime(befPrime):
        befPrime -= 1
    while not isPrime(aftPrime):
        aftPrime += 1
    return [befPrime, aftPrime]

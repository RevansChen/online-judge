# Python - 3.6.0

def sexy_prime(x, y):
    def isPrime(n):
        if n in [2, 3, 5, 7]:
            return True
        if (n < 2) or (n & 1) == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    return (abs(x - y) == 6) and isPrime(x) and isPrime(y)

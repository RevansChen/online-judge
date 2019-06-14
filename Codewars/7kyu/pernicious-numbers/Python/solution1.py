# Python - 3.6.0

pernicious = lambda n, isPrime = lambda n: (n == 2) or (n > 2) and (n & 1) and len([i for i in range(3, int(n ** 0.5) + 1, 2) if n % i == 0]) == 0: [i for i in range(3, __import__('math').floor(max(n, 0)) + 1) if isPrime(bin(i).count('1'))] or 'No pernicious numbers'

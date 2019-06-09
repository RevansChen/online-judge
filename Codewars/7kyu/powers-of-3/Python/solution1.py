# Python - 3.6.0

largestPower = lambda N, x = 3: (lambda i = int(__import__('math').log(N, x)): i + (-1) * (x ** i >= N))()

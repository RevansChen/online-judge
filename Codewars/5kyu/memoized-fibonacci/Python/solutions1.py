# Python - 3.4.3

fib = {0: 0, 1: 1}

def fibonacci(n):
    if not n in fib:
        fib[n - 2] = fibonacci(n - 2)
        fib[n - 1] = fibonacci(n - 1)
        fib[n] = fib[n - 1] + fib[n - 2]
    return fib[n]

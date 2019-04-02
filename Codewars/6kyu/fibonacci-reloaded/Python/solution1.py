# Python - 3.6.0

numbers = {1: 0, 2: 1}
maxNumber = 2
def fib(n):
    global numbers, maxNumber
    if n > maxNumber:
        for i in range(maxNumber + 1, n + 1):
            numbers[i] = numbers[i - 1] + numbers[i - 2]
        maxNumber = n
    return numbers[n]


# Python - 3.6.0

def thirt(n):
    from itertools import cycle
    
    prevNum = 0
    while True:
        prevNum = n
        c = cycle([1, 10, 9, 12, 3, 4])
        sum = 0
        while n:
            sum += next(c) * (n % 10)
            n //= 10
        if sum == prevNum:
            break
        n, prevNum = sum, n
        
    return prevNum

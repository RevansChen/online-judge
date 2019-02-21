# Python - 3.6.0

def removNb(n):
    results = []
    numbers = [*range(1, n + 1)]
    _sum = sum(numbers)
    for a in numbers:
        b, rem = divmod(_sum - a, 1 + a)
        if (rem == 0) and (b in numbers):
            results.append((a, b))
    return results

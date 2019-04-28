# Python - 3.6.0

def is_bouncy(number):
    if number <= 100:
        return False

    n = [*map(int, str(number))]
    prev = 0
    for i, curr in enumerate(n[:-1]):
        diff = n[i + 1] - curr
        if prev:
            if (prev > 0 and diff < 0) or (prev < 0 and diff > 0):
                return True
        else:
            prev = diff
    return False

# Python - 3.6.0

def close_compare(a, b, margin = 0):
    diff = a - b
    if diff == 0:
        return 0
    elif diff > 0:
        return 1 if margin < diff else 0
    else:
        return -1 if margin < -diff else 0

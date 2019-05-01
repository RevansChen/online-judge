# Python - 3.6.0

def find_2nd_largest(arr):
    arr = sorted(set(filter(lambda x: type(x) is int, arr)))
    return arr[-2] if len(arr) > 1 else None

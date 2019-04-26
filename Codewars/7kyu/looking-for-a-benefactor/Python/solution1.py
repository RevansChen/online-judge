# Python - 2.7.6

def new_avg(arr, newavg):
    n = __import__('math').ceil((len(arr) + 1) * newavg - sum(arr))
    if n <= 0:
        raise ValueError()
    return n

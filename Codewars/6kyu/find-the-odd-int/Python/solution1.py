# Python - 3.6.0

def find_it(seq):
    times = {}
    for v in seq:
        times[v] = times.get(v, 0) + 1
    for v, t in times.items():
        if t % 2:
            return v
    return None

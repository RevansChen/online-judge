# Python - 3.6.0

def max_ball(v0):
    v0 *= 1000.0 / 3600.0
    prevHeight, i = 0, 1
    while True:
        t = i * 0.1
        h = v0 * t - 0.5 * 9.81 * t * t
        if prevHeight >= h:
            return i - 1
        i += 1
        prevHeight = h
    return 0

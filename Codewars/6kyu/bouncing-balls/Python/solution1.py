# Python - 3.6.0

def bouncingBall(h, bounce, window):
    if (bounce >= 1) or (bounce <= 0) or (window >= h):
        return -1

    times = 1
    while True:
        h *= bounce
        if h < window:
            break
        times += 2
    return times

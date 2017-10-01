# Python - 3.4.3

def seven(m):
    step = 0
    while m >= 100:
        x, y = m // 10, m % 10
        m = x - 2 * y
        step += 1
    return (m, step)
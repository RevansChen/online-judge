# Python - 3.4.3

def symmetric_point(p, q):
    return [
        q[0] + (q[0] - p[0]),   # x
        q[1] + (q[1] - p[1]),   # y
    ]
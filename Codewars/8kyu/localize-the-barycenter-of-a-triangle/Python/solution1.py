# Python - 2.7.6

def sumAndDiv3(p1, p2, p3):
    return round((p1 + p2 + p3) / 3.0, 4)

def bar_triang(pointA, pointB, pointC):
    return [sumAndDiv3(pointA[i], pointB[i], pointC[i]) for i in [0, 1]]

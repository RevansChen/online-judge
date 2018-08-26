# Python3

def shapeArea(n):
    if n <= 0:
        return 0
    area = 1
    for i in range(2, n + 1):
        area += 4 * (i - 1)
    return area

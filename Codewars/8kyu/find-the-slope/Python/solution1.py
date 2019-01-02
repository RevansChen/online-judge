# Python - 2.7.6

def find_slope(points):
    dx = points[2] - points[0]
    dy = points[3] - points[1]

    return str(dy / dx) if dx else 'undefined'

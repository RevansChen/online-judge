# Python - 3.6.0

minX, maxX = 0, 1
minY, maxY = 0, 1
scale = 500
def area_of_the_shape(f):
    count = 0
    for x in range(minX, maxX * scale + 1):
        for y in range(minY, maxY * scale + 1):
            px, py = x / float(scale), y / float(scale)
            if f(px, py):
                count += 1
    return ((1.0 / scale) ** 2) * count

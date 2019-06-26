# Python - 3.6.0

find_unknown_number = lambda x, y, z: next(i for i in range(y, 106, 5) if i % 3 == x and i % 7 == z) or 105

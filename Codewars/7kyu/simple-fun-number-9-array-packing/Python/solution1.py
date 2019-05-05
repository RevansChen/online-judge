# Python - 3.6.0

array_packing = lambda arr: __import__('functools').reduce(lambda x, y: (x << 8) | y, arr[::-1])

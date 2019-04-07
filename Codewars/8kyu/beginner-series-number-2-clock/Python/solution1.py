# Python - 3.6.0

past = lambda *args: __import__('functools').reduce(lambda a, b: a * 60 + b, args) * 1000

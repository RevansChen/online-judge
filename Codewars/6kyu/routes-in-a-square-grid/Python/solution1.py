# Python - 2.7.6

prod = lambda l: reduce(lambda x, y: x * y, l)
routes = lambda n: prod(range(n + 1, 2 * n + 1)) / prod(range(1, n + 1)) if n >= 1 else 0

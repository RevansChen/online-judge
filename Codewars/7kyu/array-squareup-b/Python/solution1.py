# Python - 3.6.0

square_up = lambda n: [*__import__('itertools').chain.from_iterable([[0] * (n - i) + [*range(i, 0, -1)] for i in range(1, n + 1)])]

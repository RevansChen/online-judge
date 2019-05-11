# Python - 3.6.0

scale = lambda s, k, n: (s and '\n'.join(__import__('itertools').chain.from_iterable([''.join(map(lambda c: c * k, line))] * n for line in s.split('\n')))) or ''

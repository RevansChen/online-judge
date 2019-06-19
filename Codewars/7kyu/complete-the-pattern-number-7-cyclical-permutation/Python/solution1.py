# Python - 3.6.0

pattern = lambda n: '' if n <= 0 else '\n'.join(''.join(map(str, [*range(i + 1, n + 1)] + [*range(1, i + 1)])) for i in range(n))

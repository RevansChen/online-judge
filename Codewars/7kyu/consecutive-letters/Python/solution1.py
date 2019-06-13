# Python - 3.6.0

solve = lambda s: all(ord(b) - ord(a) == 1 for a, b in zip(sorted(s), sorted(s)[1:]))

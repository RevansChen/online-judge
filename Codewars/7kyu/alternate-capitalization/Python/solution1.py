# Python - 3.6.0

capitalize = lambda s: [''.join(c.lower() if i & 1 else c.upper() for i, c in enumerate(s)), ''.join(c.upper() if i & 1 else c.lower() for i, c in enumerate(s))]

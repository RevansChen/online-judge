# Python - 3.6.0

freq_seq = lambda s, sep: (lambda c = __import__('collections').Counter(s): sep.join(str(c[e]) for e in s))()

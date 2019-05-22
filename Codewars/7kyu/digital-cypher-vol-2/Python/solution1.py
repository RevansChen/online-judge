# Python - 3.6.0

decode = lambda code, key: ''.join(chr(ord('a') + (c - int(k) - 1) % 26) for c, k in zip(code, __import__('itertools').cycle(str(key))))

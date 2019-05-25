# Python - 3.6.0

encode = lambda message, key: [ord(c) - ord('a') + int(v) + 1 for c, v in zip(message, __import__('itertools').cycle(str(key)))]

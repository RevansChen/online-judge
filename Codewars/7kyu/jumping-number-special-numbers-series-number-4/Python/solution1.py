# Python - 3.6.0

jumping_number = lambda number: (lambda s = str(number): 'Not!!' if any(abs(x - y) != 1 for x, y in zip(map(int, s), map(int, s[1:]))) else 'Jumping!!')()

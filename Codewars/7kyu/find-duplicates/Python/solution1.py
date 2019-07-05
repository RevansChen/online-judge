# Python - 3.6.0

duplicates = lambda array: sorted([e for e in set(array) if array.count(e) > 1], key = lambda e: array.index(e, array.index(e) + 1))

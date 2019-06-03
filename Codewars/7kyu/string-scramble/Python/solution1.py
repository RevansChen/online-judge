# Python - 3.6.0

scramble = lambda string, array: ''.join(c for _, c in sorted(zip(array, string)))

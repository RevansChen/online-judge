# Python - 3.6.0

reverse = lambda arr: (lambda s = ''.join(arr)[::-1]: __import__('functools').reduce(lambda rs, e: (rs[0] + [s[rs[1]:rs[1] + len(e)]], rs[1] + len(e)), arr, ([], 0)))()[0]

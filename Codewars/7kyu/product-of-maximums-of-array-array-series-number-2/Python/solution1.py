# Python - 3.6.0

max_product = lambda lst, n: __import__('functools').reduce(int.__mul__, sorted(lst)[:-(n + 1):-1])

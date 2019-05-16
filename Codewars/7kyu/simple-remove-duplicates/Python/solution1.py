# Python - 3.6.0

solve = lambda arr: __import__('functools').reduce(lambda ls, y: ls if y in ls else (ls + [y]), arr[::-1], [])[::-1]

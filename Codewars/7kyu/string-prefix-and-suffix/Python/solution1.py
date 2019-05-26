# Python - 3.6.0

solve = lambda st: max([0] + [i for i in range(1, len(st) // 2 + 1) if st[:i] == st[-i:]])

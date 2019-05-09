# Python - 3.6.0

mystery = lambda s, n: ''.join(c for c, cond in zip(s, bin(n)[2:]) if cond == '1')

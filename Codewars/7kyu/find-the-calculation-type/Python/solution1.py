# Python - 3.6.0

calc_type = lambda a, b, res: {(op(a, b) == res): s for op, s in [(int.__add__, 'addition'), (int.__sub__, 'subtraction'), (int.__mul__, 'multiplication'), (int.__truediv__, 'division')]}[True]

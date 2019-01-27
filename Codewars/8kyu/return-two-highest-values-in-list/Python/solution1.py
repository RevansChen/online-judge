# Python - 3.6.0

two_highest = lambda arg: sorted(list(set(arg)), reverse=True)[:2] if type(arg) is list else False

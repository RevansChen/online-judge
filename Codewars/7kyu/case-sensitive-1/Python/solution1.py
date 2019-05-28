# Python - 3.6.0

case_sensitive = lambda s: (lambda uc = [*filter(str.isupper, s)]: [len(uc) == 0, uc])()

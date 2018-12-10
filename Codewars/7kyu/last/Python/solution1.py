# Python - 3.6.0

def last(*e):
    if len(e) == 1:
        if hasattr(e[0], '__getitem__'):
            return e[0][-1]
        else:
            return e[0]
    else:
        return e[-1]

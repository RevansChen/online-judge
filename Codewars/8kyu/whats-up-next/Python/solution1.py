# Python - 3.6.0

def next_item(xs, item):
    try:
        it = iter(xs)
        for e in it:
            if e == item:
                return next(it)
    except:
        pass
    return None

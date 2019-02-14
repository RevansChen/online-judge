# Python - 3.6.0

def unique_in_order(iterable):
    if len(iterable) == 0:
        return []

    cmp = iterable[0]
    result = [cmp]
    for e in iterable[1:]:
        if cmp != e:
            result.append(e)
            cmp = e
    return result

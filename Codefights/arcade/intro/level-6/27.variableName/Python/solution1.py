# Python3

def variableName(name):
    from functools import reduce
    isCorrectChar = lambda c: c.isdigit() or c.isalpha() or c == '_'
    if name[0].isalpha() or name[0] == '_':
        if len(name[1:]):
            return reduce(lambda x, y: x and y, [ isCorrectChar(c) for c in name[1:] ])
        return True
    return False

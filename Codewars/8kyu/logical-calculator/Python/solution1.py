# Python - 2.7.6

def logical_calc(array, op):
    logic = {
        'AND': lambda a, b: a and b,
        'OR':  lambda a, b: a or b,
        'XOR': lambda a, b: a != b
    }
    return reduce(lambda a, b: logic.get(op, lambda *_: False)(a, b), array)

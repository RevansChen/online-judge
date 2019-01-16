# Python - 2.7.6

def logical_calc(array, op):
    logic = {
        'AND': all,
        'OR':  any,
        'XOR': lambda arr: bool(arr.count(True) & 1)
    }
    if op in logic:
        return logic[op](array)
    return False

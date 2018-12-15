# Python - 3.6.0

operators = {
    '+' : lambda a, b: a + b,
    '-' : lambda a, b: a - b,
    '*' : lambda a, b: a * b,
    '/' : lambda a, b: a / b
}
def basic_op(operator, value1, value2):
    return operators[operator](value1, value2)

# Python - 3.4.3

def calculator(x, y, op):
    # 使用根據運算子建立對應的lambda並執行
    return {
        '+': lambda: x + y,
        '-': lambda: x - y,
        '*': lambda: x * y,
        '/': lambda: x / y
    }.get(op, lambda: 'unknown value')()
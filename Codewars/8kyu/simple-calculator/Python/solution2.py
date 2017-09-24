# Python - 3.4.3

def calculator(x, y, op):
    # 使用根據運算子建立對應的計算值並回傳
    return {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y
    }.get(op, 'unknown value')
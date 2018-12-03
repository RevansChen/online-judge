# Python - 3.6.0

def my_first_interpreter(code):
    value = 0
    output = ''
    for c in code:
        if c == '+':
            value = (value + 1) & 0xFF
        elif c == '.':
            output += chr(value)
    return output

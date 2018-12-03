# Python - 3.6.0

def my_first_interpreter(code):
    memory = [0]
    output = ''
    pointer = 0
    for c in code:
        if c == '+':
            memory[pointer] = (memory[pointer] + 1) & 0xFF
        elif c == '.':
            output += chr(memory[pointer])
    return output

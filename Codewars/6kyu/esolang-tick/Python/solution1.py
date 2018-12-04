# Python - 3.6.0

def interpreter(tape):
    output = ''
    memory = {}
    index = 0
    for t in tape:
        if t == '>':
            index += 1
        elif t == '<':
            index -= 1
        elif t == '+':
            memory[index] = ((memory[index] + 1) & 255) if index in memory else 1
        elif t == '*':
            output += chr(memory[index])

    return output

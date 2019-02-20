# Python - 3.6.0

def interpreter(tape):
    output = ''
    stack = [0]
    index = 0
    while index < len(tape):
        cmd = tape[index]
        if cmd == '^':
            stack.pop()
        elif cmd == '!':
            stack.append(0)
        elif cmd == '+':
            stack[-1] = (stack[-1] + 1) % 256
        elif cmd == '-':
            stack[-1] = (stack[-1] - 1) % 256
        elif cmd == '*':
            output += chr(stack[-1])
        elif cmd == '[':
            if stack[-1] == 0:
                index = tape[index:].index(']')
        elif cmd == ']':
            if stack[-1] != 0:
                index = tape[:index].index('[')
        index += 1
    return output

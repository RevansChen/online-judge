# Python - 3.6.0

def presses(phrase):
    keypads = ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', '*', ' 0', '#']
    times, i = 0, 0
    for p in phrase.upper():
        for keypad in keypads:
            i = keypad.find(p)
            if i >= 0:
                break
        times += i + 1
    return times

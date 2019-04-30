# Python - 3.6.0

def tail_swap(strings):
    s1, s2 = strings
    a, b = s1.split(':')
    c, d = s2.split(':')
    return [f'{a}:{d}', f'{c}:{b}']

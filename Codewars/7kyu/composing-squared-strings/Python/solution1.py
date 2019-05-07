# Python - 3.6.0

def compose(s1, s2):
    l1, l2 = s1.split('\n'), s2.split('\n')
    return '\n'.join([
        l1[i][:i + 1] + l2[-(i + 1)][:len(l1) - i] for i in range(len(l1))
    ])

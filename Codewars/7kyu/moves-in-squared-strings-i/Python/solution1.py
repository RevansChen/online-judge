# Python - 3.6.0

vert_mirror = lambda s: '\n'.join(line[::-1] for line in s.split('\n'))
hor_mirror = lambda s: '\n'.join(s.split('\n')[::-1])
oper = lambda f, s: f(s)

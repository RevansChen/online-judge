# Python3

from solution1 import repeatChar as f

qa = [
    ('*', 20,
     '********************'),
    ('!', 10,
     '!!!!!!!!!!'),
    ('#', 11,
     '###########'),
    ('?', 20,
     '????????????????????'),
    ('@', 12,
     '@@@@@@@@@@@@'),
    ('x', 0,
     '')
]

for *q, a in qa:
    for i, e in enumerate(q):
        print('input{0}: {1}'.format(i + 1, e))
    ans = f(*q)
    if ans != a:
        print('  [failed]')
        print('    output:', ans)
        print('    expected:', a)
    else:
        print('  [ok]')
        print('    output:', ans)
    print()

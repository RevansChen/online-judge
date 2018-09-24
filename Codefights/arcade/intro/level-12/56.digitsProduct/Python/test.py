# Python3

from solution1 import digitsProduct as f

qa = [
    (12, 26),
    (19, -1),
    (450, 2559),
    (0, 10),
    (13, -1),
    (1, 1),
    (243, 399),
    (576, 889),
    (360, 589)
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

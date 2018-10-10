# Python3

from solution1 import rangeBitCount as f

qa = [
    (2, 7, 11),
    (0, 1, 1),
    (1, 10, 17),
    (8, 9, 3),
    (9, 10, 4)
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

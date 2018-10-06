# Python3

from solution2 import phoneCall as f

qa = [
    (3, 1, 2, 20, 14),
    (2, 2, 1, 2, 1),
    (10, 1, 2, 22, 11),
    (2, 2, 1, 24, 14),
    (1, 2, 1, 6, 3)
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

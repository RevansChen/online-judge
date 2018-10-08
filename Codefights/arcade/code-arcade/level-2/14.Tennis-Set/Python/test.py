# Python3

from solution1 import tennisSet as f

qa = [
    (3, 6, True),
    (8, 5, False),
    (6, 5, False),
    (7, 7, False),
    (6, 4, True),
    (7, 5, True),
    (7, 2, False),
    (7, 6, True),
    (4, 10, False),
    (0, 0, False)
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

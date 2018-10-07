# Python3

from solution1 import isInfiniteProcess as f

qa = [
    (2, 6, False),
    (2, 3, True),
    (2, 10, False),
    (0, 1, True),
    (3, 1, True),
    (10, 10, False),
    (5, 10, True),
    (6, 10, False),
    (10, 0, True),
    (5, 5, False)
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

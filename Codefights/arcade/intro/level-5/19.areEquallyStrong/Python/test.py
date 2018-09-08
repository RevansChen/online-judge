# Python3

from solution1 import areEquallyStrong as f

qa = [
    (10, 15, 15, 10, True),
    (15, 10, 15, 10, True),
    (15, 10, 15, 9, False),
    (10, 5, 5, 10, True),
    (10, 15, 5, 20, False),
    (10, 20, 10, 20, True),
    (5, 20, 20, 5, True),
    (20, 15, 5, 20, False),
    (5, 10, 5, 10, True),
    (1, 10, 10, 0, False),
    (5, 5, 10, 10, False),
    (10, 5, 10, 6, False),
    (1, 1, 1, 1, True),
    (0, 10, 10, 0, True)
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

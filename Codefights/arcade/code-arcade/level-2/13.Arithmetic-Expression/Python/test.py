# Python3

from solution2 import arithmeticExpression as f

qa = [
    (2, 3, 5, True),
    (8, 2, 4, True),
    (8, 2, 3, False),
    (6, 3, 3, True),
    (18, 2, 9, True),
    (2, 3, 6, True),
    (5, 2, 0, False),
    (10, 2, 2, False),
    (5, 2, 2, False),
    (1, 2, 1, False)
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

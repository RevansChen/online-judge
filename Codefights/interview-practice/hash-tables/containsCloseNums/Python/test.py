# Python3

from solution1 import containsCloseNums as f

qa = [
    ([0, 1, 2, 3, 5, 2], 3, True),
    ([0, 1, 2, 3, 5, 2], 2, False),
    ([], 0, False),
    ([99, 99], 2, True),
    ([2, 2], 3, True),
    ([1, 2], 2, False),
    ([1, 2, 1], 2, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 1], 0, False),
    ([1, 2, 1], 1, False),
    ([1], 1, False),
    ([-1, -1], 1, True)
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

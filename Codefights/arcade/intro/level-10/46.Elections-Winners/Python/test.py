# Python3

from solution1 import electionsWinners as f

qa = [
    ([2, 3, 5, 2], 3, 2),
    ([1, 3, 3, 1, 1], 0, 0),
    ([5, 1, 3, 4, 1], 0, 1),
    ([1, 1, 1, 1], 1, 4),
    ([1, 1, 1, 1], 0, 0),
    ([3, 1, 1, 3, 1], 2, 2)
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

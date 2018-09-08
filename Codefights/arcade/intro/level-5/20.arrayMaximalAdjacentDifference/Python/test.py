# Python3

from solution1 import arrayMaximalAdjacentDifference as f

qa = [
    ([2, 4, 1, 0], 3),
    ([1, 1, 1, 1], 0),
    ([-1, 4, 10, 3, -2], 7),
    ([10, 11, 13], 2),
    ([-2, -2, -2, -2, -2], 0),
    ([-1, 1, -3, -4], 4)
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

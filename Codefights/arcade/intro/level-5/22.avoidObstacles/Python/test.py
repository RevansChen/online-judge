# Python3

from solution1 import avoidObstacles as f

qa = [
    ([5, 3, 6, 7, 9], 4),
    ([2, 3], 4),
    ([1, 4, 10, 6, 2], 7),
    ([1000, 999], 6),
    ([19, 32, 11, 23], 3),
    ([5, 8, 9, 13, 14], 6)
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

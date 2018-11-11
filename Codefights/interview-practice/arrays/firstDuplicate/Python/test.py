# Python3

from solution1 import firstDuplicate as f

qa = [
    ([2, 1, 3, 5, 3, 2], 3),
    ([2, 4, 3, 5, 1], -1),
    ([1], -1),
    ([2, 2], 2),
    ([2, 1], -1),
    ([2, 1, 3], -1),
    ([2, 3, 3], 3),
    ([3, 3, 3], 3),
    ([8, 4, 6, 2, 6, 4, 7, 9, 5, 8], 6),
    ([10, 6, 8, 4, 9, 1, 7, 2, 5, 3], -1),
    ([1, 1, 2, 2, 1], 1)
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

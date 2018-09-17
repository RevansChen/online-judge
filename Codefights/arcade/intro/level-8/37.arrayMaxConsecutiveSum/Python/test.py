# Python3

from solution1 import arrayMaxConsecutiveSum as f

qa = [
    ([2, 3, 5, 1, 6], 2, 8),
    ([2, 4, 10, 1], 2, 14),
    ([1, 3, 2, 4], 3, 9),
    ([3, 2, 1, 1], 1, 3)
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

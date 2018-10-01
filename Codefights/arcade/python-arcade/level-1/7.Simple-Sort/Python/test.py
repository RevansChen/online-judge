# Python3

from solution1 import simpleSort as f

qa = [
    ([2, 4, 1, 5], [1, 2, 4, 5]),
    ([3, 6, 1, 5, 3, 6], [1, 3, 3, 5, 6, 6]),
    ([100], [100]),
    ([-1, -2, 0], [-2, -1, 0])
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

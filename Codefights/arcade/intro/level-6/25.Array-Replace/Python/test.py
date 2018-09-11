# Python3

from solution1 import arrayReplace as f

qa = [
    ([1, 2, 1], 1, 3,
     [3, 2, 3]),
    ([1, 2, 3, 4, 5], 3, 0,
     [1, 2, 0, 4, 5]),
    ([1, 1, 1], 1, 10,
     [10, 10, 10]),
    ([1, 2, 1, 2, 1], 2, 1,
     [1, 1, 1, 1, 1]),
    ([1, 2, 1, 2, 1], 2, 2,
     [1, 2, 1, 2, 1]),
    ([3, 1], 3, 9,
     [9, 1])
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

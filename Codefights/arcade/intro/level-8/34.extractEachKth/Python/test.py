# Python3

from solution1 import extractEachKth as f

qa = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3,
     [1, 2, 4, 5, 7, 8, 10]),
    ([1, 1, 1, 1, 1], 1,
     []),
    ([1, 2, 1, 2, 1, 2, 1, 2], 2,
     [1, 1, 1, 1]),
    ([1, 2, 1, 2, 1, 2, 1, 2], 10,
     [1, 2, 1, 2, 1, 2, 1, 2]),
    ([2, 4, 6, 8, 10], 2,
     [2, 6, 10])
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

# Python3

from solution1 import adjacentElementsProduct as f

qa = [
    ([3, 6, -2, -5, 7, 3], 21),
    ([-1, -2], 2),
    ([5, 1, 2, 3, 1, 4], 6),
    ([1, 2, 3, 0], 6),
    ([9, 5, 10, 2, 24, -1, -48], 50),
    ([5, 6, -4, 2, 3, 2, -23], 30),
    ([4, 1, 2, 3, 1, 5], 6),
    ([-23, 4, -3, 8, -12], -12),
    ([1, 0, 1, 0, 1000], 0)
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

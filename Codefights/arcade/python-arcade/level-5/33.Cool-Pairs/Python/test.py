# Python3

from solution1 import coolPairs as f

qa = [
    ([4, 5, 6, 7, 8], [8, 9, 10, 11, 12], 2),
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 4),
    ([2], [2], 1),
    ([7, 8, 9], [5, 3, 2], 0),
    ([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [1, 2, 3, 4, 5], 2)
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

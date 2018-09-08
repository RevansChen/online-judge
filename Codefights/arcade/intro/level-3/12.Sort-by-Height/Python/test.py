# Python3

from solution1 import sortByHeight as f

qa = [
    ([-1, 150, 190, 170, -1, -1, 160, 180],
     [-1, 150, 160, 170, -1, -1, 180, 190]),
    ([-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1]),
    ([-1],
     [-1]),
    ([4, 2, 9, 11, 2, 16],
     [2, 2, 4, 9, 11, 16]),
    ([2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1],
     [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]),
    ([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3],
     [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77])
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

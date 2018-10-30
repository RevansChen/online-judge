# Python3

from solution1 import correctLineup as f

qa = [
    ([1, 2, 3, 4, 5, 6],
     [2, 1, 4, 3, 6, 5]),
    ([13, 42],
     [42, 13]),
    ([2, 3, 1, 100, 99, 45, 22, 28],
     [3, 2, 100, 1, 45, 99, 28, 22]),
    ([85, 32, 45, 67, 32, 12, 45, 67],
     [32, 85, 67, 45, 12, 32, 67, 45]),
    ([60, 2, 24, 40],
     [2, 60, 40, 24])
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

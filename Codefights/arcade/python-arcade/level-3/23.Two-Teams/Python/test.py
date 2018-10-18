# Python3

from solution1 import twoTeams as f

qa = [
    ([1, 11, 13, 6, 14],
     11),
    ([3, 4],
     -1),
    ([16, 14, 79, 8, 71, 72, 71, 10, 80, 76, 83, 70, 57, 29, 31],
     209),
    ([23, 72, 54, 4, 88, 91, 8, 44],
     -38),
    ([23, 74, 57, 33, 61, 99, 19, 12, 19, 38, 77, 70, 20],
     -50)
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

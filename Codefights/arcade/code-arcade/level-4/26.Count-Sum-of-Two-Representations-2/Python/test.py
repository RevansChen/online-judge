# Python3

from solution1 import countSumOfTwoRepresentations2 as f

qa = [
    (6, 2, 4, 2),
    (6, 3, 3, 1),
    (10, 9, 11, 0),
    (24, 8, 16, 5),
    (24, 12, 12, 1),
    (93, 24, 58, 12)
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

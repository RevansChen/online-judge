# Python3

from solution1 import secondRightmostZeroBit as f

qa = [
    (37, 8),
    (1073741824, 2),
    (83748, 2),
    (4, 2),
    (728782938, 4)
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

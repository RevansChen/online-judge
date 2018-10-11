# Python3

from solution1 import differentRightmostBit as f

qa = [
    (11, 13, 2),
    (7, 23, 16),
    (1, 0, 1),
    (64, 65, 1),
    (1073741823, 1071513599, 131072),
    (42, 22, 4)
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

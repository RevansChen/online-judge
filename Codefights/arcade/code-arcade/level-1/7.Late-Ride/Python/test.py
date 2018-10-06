# Python3

from solution1 import lateRide as f

qa = [
    (240, 4),
    (808, 14),
    (1439, 19),
    (0, 0),
    (23, 5),
    (8, 8)
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

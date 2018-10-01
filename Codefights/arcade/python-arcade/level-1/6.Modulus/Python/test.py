# Python3

from solution1 import modulus as f

qa = [
    (15, 1),
    (23.12, -1),
    (0, 0),
    (232.2423, -1),
    (30, 0),
    (11, 1)
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

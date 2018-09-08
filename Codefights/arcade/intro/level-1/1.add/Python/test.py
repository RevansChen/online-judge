# Python3

from solution1 import add as f

qa = [
    (1, 2, 3),
    (0, 1000, 1000),
    (2, -39, -37),
    (99, 100, 199),
    (-100, 100, 0),
    (-1000, -1000, -2000)
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

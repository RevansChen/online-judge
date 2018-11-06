# Python3

from solution1 import sign as f

qa = [
    (-34, -1),
    (42, 1),
    (0, 0),
    (-50, -1),
    (50, 1)
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

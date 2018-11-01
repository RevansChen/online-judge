# Python3

from solution1 import primesSum as f

qa = [
    (10, 20, 60),
    (1, 7, 17),
    (5, 10, 12),
    (24, 28, 0),
    (13, 13, 13)
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

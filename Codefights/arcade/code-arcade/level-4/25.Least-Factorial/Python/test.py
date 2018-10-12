# Python3

from solution1 import leastFactorial as f

qa = [
    (17, 24),
    (1, 1),
    (5, 6),
    (25, 120),
    (18, 24),
    (109, 120),
    (106, 120),
    (11, 24),
    (55, 120),
    (24, 24)
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

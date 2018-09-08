# Python3

from solution1 import centuryFromYear as f

qa = [
    (1905, 20),
    (1700, 17),
    (1988, 20),
    (2000, 20),
    (2001, 21),
    (200, 2),
    (374, 4),
    (45, 1),
    (8, 1)
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

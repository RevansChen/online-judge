# Python3

from solution1 import maxMultiple as f

qa = [
    (3, 10, 9),
    (2, 7, 6),
    (10, 50, 50),
    (7, 100, 98)
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

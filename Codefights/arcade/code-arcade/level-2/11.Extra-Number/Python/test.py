# Python3

from solution1 import extraNumber as f

qa = [
    (2, 7, 2, 7),
    (3, 2, 2, 3),
    (5, 5, 1, 1),
    (500000000, 3, 500000000, 3)
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

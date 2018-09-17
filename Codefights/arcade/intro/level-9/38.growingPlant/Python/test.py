# Python3

from solution1 import growingPlant as f

qa = [
    (100, 10, 910, 10),
    (10, 9, 4, 1),
    (5, 2, 7, 2),
    (7, 3, 443, 110),
    (6, 5, 10, 5)
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

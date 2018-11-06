# Python3

from solution1 import primarySchool as f

qa = [
    (7, 4, '7 x 4 = 28'),
    (1, 20, '1 x 20 = 20'),
    (3, 13, '3 x 13 = 39'),
    (10, 3, '10 x 3 = 30'),
    (16, 12, '16 x 12 = 192')
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

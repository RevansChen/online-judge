# Python3

from solution1 import knapsackLight as f

qa = [
    (10, 5, 6, 4, 8, 10),
    (10, 5, 6, 4, 9, 16),
    (5, 3, 7, 4, 6, 7),
    (10, 2, 11, 3, 1, 0),
    (15, 2, 20, 3, 2, 15),
    (2, 5, 3, 4, 5, 3),
    (4, 3, 3, 4, 4, 4),
    (3, 5, 3, 8, 10, 3)
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

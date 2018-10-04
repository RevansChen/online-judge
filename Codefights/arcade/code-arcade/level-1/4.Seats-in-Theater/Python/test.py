# Python3

from solution1 import seatsInTheater as f

qa = [
    (16, 11, 5, 3, 96),
    (1, 1, 1, 1, 0),
    (13, 6, 8, 3, 18),
    (60, 100, 60, 1, 99),
    (1000, 1000, 1000, 1000, 0)
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

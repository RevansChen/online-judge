# Python3

from solution1 import depositProfit as f

qa = [
    (100, 20, 170, 3),
    (100, 1, 101, 1),
    (1, 100, 64, 6),
    (20, 20, 50, 6),
    (50, 25, 100, 4)
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

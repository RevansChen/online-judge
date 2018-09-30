# Python3

from solution1 import countBits as f

qa = [
    (50, 6),
    (1, 1),
    (1000000000, 30),
    (237487384, 28),
    (278, 9)
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

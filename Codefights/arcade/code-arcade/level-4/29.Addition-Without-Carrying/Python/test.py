# Python3

from solution1 import additionWithoutCarrying as f

qa = [
    (456, 1734, 1180),
    (99999, 0, 99999),
    (999, 999, 888),
    (0, 0, 0),
    (54321, 54321, 8642)
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

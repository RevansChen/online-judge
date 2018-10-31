# Python3

from solution1 import prefSum as f

qa = [
    ([1, 2, 3],
     [1, 3, 6]),
    ([1, 2, 3, -6],
     [1, 3, 6, 0]),
    ([0, 0, 0],
     [0, 0, 0])
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

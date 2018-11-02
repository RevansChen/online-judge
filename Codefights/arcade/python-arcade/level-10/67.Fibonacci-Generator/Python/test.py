# Python3

from solution1 import fibonacciGenerator as f

qa = [
    (3, [0, 1, 1]),
    (1, [0]),
    (7, [0, 1, 1, 2, 3, 5, 8])
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

# Python3

from solution1 import circleOfNumbers as f

qa = [
    (10, 2, 7),
    (10, 7, 2),
    (4, 1, 3),
    (6, 3, 0)
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

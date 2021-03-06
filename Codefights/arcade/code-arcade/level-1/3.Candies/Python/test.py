# Python3

from solution1 import candies as f

qa = [
    (3, 10, 9),
    (1, 2, 2),
    (10, 5, 0),
    (4, 4, 4)
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

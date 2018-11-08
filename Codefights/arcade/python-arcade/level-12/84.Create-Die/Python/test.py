# Python3

from solution1 import createDie as f

qa = [
    (37237, 5, 3),
    (36706, 12, 9),
    (21498, 10, 10),
    (2998, 6, 3),
    (5509, 10, 4)
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

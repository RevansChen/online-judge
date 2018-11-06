# Python3

from solution1 import countVisitors as f

qa = [
    (22, 5, [4, 6, 6, 5, 2, 2, 5], 26),
    (1, 5, [], 1),
    (34, 8, [1, 2, 3, 4, 5, 6, 7], 34),
    (4, 5, [3, 4, 65, 3, 2, 4, 5, 3, 5], 7),
    (38, 20, [20], 39)
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

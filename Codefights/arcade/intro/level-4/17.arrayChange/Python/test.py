# Python3

from solution1 import arrayChange as f

qa = [
    ([1, 1, 1], 3),
    ([-1000, 0, -2, 0], 5),
    ([2, 1, 10, 1], 12),
    ([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15], 13)
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

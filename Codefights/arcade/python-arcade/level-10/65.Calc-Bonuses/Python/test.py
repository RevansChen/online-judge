# Python3

from solution1 import calcBonuses as f

qa = [
    ([4, 2, 4, 5], 3, 10),
    ([4, 2, 4, 5], 5, 0),
    ([], 5, 0),
    ([5, 3, 1, 9], 4, 18),
    ([3, 9, 0, 50], 1, 3),
    ([8, 8, 39, 33, 29, 35], 4, 88)
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

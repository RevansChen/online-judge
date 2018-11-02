# Python3

from solution1 import calcFinalScore as f

qa = [
    ([4, 2, 4, 5], 3, 57),
    ([4, 2, 4, 5], 5, 12),
    ([], 5, 0),
    ([5, 3, 1, 9], 4, 116),
    ([3, 9, 0, 50], 1, 2500),
    ([8, 8, 39, 33, 29, 35], 4, 4676)
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

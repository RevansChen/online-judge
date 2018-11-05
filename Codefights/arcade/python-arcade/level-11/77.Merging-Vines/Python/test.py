# Python3

from solution1 import mergingVines as f

qa = [
    ([1, 2, 3, 4, 5], 2, [10, 5]),
    ([1, 2, 3, 4, 5, 6], 10, [21]),
    ([5], 4, [5]),
    ([43, 54, 8, 12, 0, 12, 7, 7, 4], 0, [43, 54, 8, 12, 0, 12, 7, 7, 4]),
    ([13, 11, 9, 5, 7, 5, 12, 10, 1, 2, 11, 2, 10, 10, 18, 16, 20, 13, 9, 100], 4, [142, 142])
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

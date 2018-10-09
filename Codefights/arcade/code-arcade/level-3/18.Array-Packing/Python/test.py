# Python3

from solution1 import arrayPacking as f

qa = [
    ([24, 85, 0], 21784),
    ([23, 45, 39], 2567447),
    ([1, 2, 4, 8], 134480385),
    ([5], 5),
    ([187, 99, 42, 43], 724198331)
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

# Python3

from solution1 import makeArrayConsecutive2 as f

qa = [
    ([6, 2, 3, 8], 3),
    ([0, 3], 2),
    ([5, 4, 6], 0),
    ([1], 0)
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

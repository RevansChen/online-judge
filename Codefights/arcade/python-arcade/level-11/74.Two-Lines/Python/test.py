# Python3

from solution1 import twoLines as f

qa = [
    ([1, 2], [2, 1], 0, 2, 'any'),
    ([1, 2], [2, 1], -1, 2, 'first'),
    ([1, 2], [2, 1], 0, 3, 'second'),
    ([1, 2], [1, 0], -1000, 1000, 'first'),
    ([1, 0], [-1, 0], -239, 239, 'any'),
    ([1, 0], [-1, 0], -999, 998, 'second')
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

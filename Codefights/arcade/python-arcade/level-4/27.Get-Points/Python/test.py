# Python3

from solution1 import getPoints as f

qa = [
    ([True, True, False, True],
     2, 5),
    ([True, False, True, False],
     7, -10),
    ([True, False],
     0, 1),
    ([True, True, True, False, True, True, True, False, True, True, True, True, False],
     2, 60),
    ([False, True, True, True, False, True],
     1, 13),
    ([False],
     10, -10)
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

# Python3

from solution1 import isLucky as f

qa = [
    (1230, True),
    (239017, False),
    (134008, True),
    (10, False),
    (11, True),
    (1010, True),
    (261534, False),
    (100000, False),
    (999999, True),
    (123321, True)
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

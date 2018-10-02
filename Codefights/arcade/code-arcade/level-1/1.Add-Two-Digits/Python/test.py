# Python3

from solution1 import addTwoDigits as f

qa = [
    (29, 11),
    (48, 12),
    (10, 1),
    (25, 7)
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

# Python3

from solution1 import appleBoxes as f

qa = [
    (5, -15),
    (15, -120),
    (36, 666),
    (1, -1)
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

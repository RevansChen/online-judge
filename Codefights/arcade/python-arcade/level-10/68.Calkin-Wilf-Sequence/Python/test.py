# Python3

from solution1 import calkinWilfSequence as f

qa = [
    ([1, 3], 3),
    ([1, 1], 0),
    ([3, 1], 6),
    ([14, 3], 110),
    ([7, 13], 129)
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

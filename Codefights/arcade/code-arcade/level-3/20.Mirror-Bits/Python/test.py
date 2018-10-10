# Python3

from solution1 import mirrorBits as f

qa = [
    (97, 67),
    (8, 1),
    (123, 111),
    (86782, 65173),
    (5, 5)
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

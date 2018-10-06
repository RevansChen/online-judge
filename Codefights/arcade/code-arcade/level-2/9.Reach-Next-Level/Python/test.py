# Python3

from solution1 import reachNextLevel as f

qa = [
    (10, 15, 5, True),
    (10, 15, 4, False),
    (3, 6, 4, True),
    (84, 135, 36, False),
    (74, 170, 58, False),
    (80, 199, 15, False),
    (97, 57, 7, True),
    (235, 293, 4, False),
    (222, 137, 58, True),
    (16, 23, 16, True)
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

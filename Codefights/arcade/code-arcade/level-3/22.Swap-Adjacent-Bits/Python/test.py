# Python3

from solution1 import swapAdjacentBits as f

qa = [
    (13, 14),
    (74, 133),
    (1073741823, 1073741823),
    (0, 0),
    (1, 2),
    (83748, 166680)
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

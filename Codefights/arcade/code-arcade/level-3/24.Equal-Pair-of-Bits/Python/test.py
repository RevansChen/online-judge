# Python3

from solution1 import equalPairOfBits as f

qa = [
    (10, 11, 2),
    (0, 0, 1),
    (28, 27, 8),
    (895, 928, 32),
    (1073741824, 1006895103, 262144)
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

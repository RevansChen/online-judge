# Python3

from solution2 import magicalWell as f

qa = [
    (1, 2, 2, 8),
    (1, 1, 1, 1),
    (6, 5, 3, 128),
    (1601, 337, 0, 0),
    (1891, 352, 0, 0),
    (1936, 1835, 5, 17800540),
    (957, 57, 2, 110113),
    (687, 1337, 0, 0),
    (491, 1552, 4, 3060400),
    (1275, 362, 2, 924738)
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

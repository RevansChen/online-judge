# Python3

from solution1 import lineUp as f

qa = [
    ('LLARL', 3),
    ('RLR', 1),
    ('', 0),
    ('L', 0),
    ('A', 1),
    ('AAAAAAAAAAAAAAA', 15),
    ('RRRRRRRRRRLLLLLLLLLRRRRLLLLLLLLLL', 16),
    ('AALAAALARAR', 5)
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

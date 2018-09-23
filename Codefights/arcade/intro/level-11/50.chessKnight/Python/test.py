# Python3

from solution1 import chessKnight as f

qa = [
    ('a1', 2),
    ('c2', 6),
    ('d4', 8),
    ('g6', 6)
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

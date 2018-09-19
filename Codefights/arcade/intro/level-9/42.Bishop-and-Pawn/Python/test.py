# Python3

from solution1 import bishopAndPawn as f

qa = [
    ('a1', 'c3', True),
    ('h1', 'h3', False),
    ('a5', 'c3', True),
    ('g1', 'f3', False),
    ('e7', 'd6', True),
    ('e7', 'a3', True),
    ('e3', 'a7', True),
    ('a1', 'h8', True),
    ('a1', 'h7', False),
    ('h1', 'a8', True)
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

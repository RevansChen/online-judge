# Python3

from solution1 import chessBoardCellColor as f

qa = [
    ('A1', 'C3', True),
    ('A1', 'H3', False),
    ('A1', 'A2', False),
    ('A1', 'B2', True),
    ('B3', 'H8', False),
    ('C3', 'B5', False),
    ('G5', 'E7', True),
    ('C8', 'H8', False),
    ('D2', 'D2', True),
    ('A2', 'A5', False)
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

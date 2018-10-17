# Python3

from solution1 import competitiveEating as f

qa = [
    (3.1415, 10, 2,
     '   3.14   '),
    (29.8245, 10, 0,
     '    30    '),
    (9.34, 4, 2,
     '9.34'),
    (837.28472, 20, 7,
     '    837.2847200     '),
    (0, 4, 1,
     '0.0 '),
    (1, 3, 0,
     ' 1 '),
    (666.2837, 15, 1,
     '     666.3     ')
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

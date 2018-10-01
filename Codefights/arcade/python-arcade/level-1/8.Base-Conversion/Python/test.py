# Python3

from solution1 import baseConversion as f

qa = [
    ('1302', 5, 'ca'),
    ('1010100101', 2, '2a5'),
    ('z', 36, '23'),
    ('30', 4, 'c'),
    ('6', 7, '6'),
    ('337', 8, 'df'),
    ('ab3f', 16, 'ab3f'),
    ('0', 2, '0'),
    ('ci', 19, 'f6'),
    ('8c4897', 13, '32b5cc')
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

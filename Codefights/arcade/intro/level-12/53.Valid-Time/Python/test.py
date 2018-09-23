# Python3

from solution1 import validTime as f

qa = [
    ('13:58', True),
    ('25:51', False),
    ('02:76', False),
    ('24:00', False),
    ('02:61', False),
    ('27:00', False),
    ('19:66', False),
    ('12:31', True),
    ('25:73', False),
    ('09:56', True)
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

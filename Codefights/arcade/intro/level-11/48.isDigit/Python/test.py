# Python3

from solution1 import isDigit as f

qa = [
    ('0', True),
    ('-', False),
    ('O', False),
    ('1', True),
    ('2', True),
    ('!', False),
    ('@', False),
    ('+', False),
    ('6', True),
    ('(', False),
    (')', False)
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

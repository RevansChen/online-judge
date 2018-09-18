# Python3

from solution1 import longestDigitsPrefix as f

qa = [
    ('123aa1', '123'),
    ('0123456789', '0123456789'),
    ('  3) always check for whitespaces', ''),
    ('12abc34', '12'),
    ('the output is 42', '')
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

# Python3

from solution1 import firstDigit as f

qa = [
    ('var_1__Int', '1'),
    ('q2q-q', '2'),
    ('0ss', '0'),
    ('_Aas_23', '2'),
    ('a a_933', '9'),
    ('ok0', '0')
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

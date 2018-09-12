# Python3

from solution1 import variableName as f

qa = [
    ('var_1__Int', True),
    ('qq-q', False),
    ('2w2', False),
    (' variable', False),
    ('va[riable0', False),
    ('variable0', True),
    ('a', True),
    ('_Aas_23', True),
    ('a a_2', False),
    ('0ss', False)
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

# Python3

from solution1 import userAttribute as f

qa = [
    ('_id', '1234567'),
    ('age', 'age attribute is not defined'),
    ('name', 'anny'),
    ('country', 'country attribute is not defined'),
    ('I', 'I attribute is not defined')
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

# Python3

from solution1 import isBeautifulString as f

qa = [
    ('bbbaacdafe', True),
    ('aabbb', False),
    ('bbc', False),
    ('bbbaa', False),
    ('abcdefghijklmnopqrstuvwxyzz', False),
    ('abcdefghijklmnopqrstuvwxyz', True),
    ('abcdefghijklmnopqrstuvwxyzqwertuiopasdfghjklxcvbnm', True),
    ('fyudhrygiuhdfeis', False),
    ('zaa', False),
    ('zyy', False)
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

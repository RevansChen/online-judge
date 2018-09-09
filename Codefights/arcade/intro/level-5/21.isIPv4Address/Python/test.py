# Python3

from solution1 import isIPv4Address as f

qa = [
    ('172.16.254.1', True),
    ('172.316.254.1', False),
    ('.254.255.0', False),
    ('1.1.1.1a', False),
    ('1', False),
    ('0.254.255.0', True),
    ('1.23.256.255.', False),
    ('1.23.256..', False),
    ('0..1.0', False),
    ('1.1.1.1.1', False),
    ('1.256.1.1', False),
    ('a0.1.1.1', False),
    ('0.1.1.256', False),
    ('129380129831213981.255.255.255', False),
    ('255.255.255.255abcdekjhf', False),
    ('7283728', False)
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

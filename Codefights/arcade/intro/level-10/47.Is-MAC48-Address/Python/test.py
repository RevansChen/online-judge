# Python3

from solution1 import isMAC48Address as f

qa = [
    ('00-1B-63-84-45-E6', True),
    ('Z1-1B-63-84-45-E6', False),
    ('not a MAC-48 address', False),
    ('FF-FF-FF-FF-FF-FF', True),
    ('00-00-00-00-00-00', True),
    ('G0-00-00-00-00-00', False),
    ('02-03-04-05-06-07-', False),
    ('12-34-56-78-9A-BC', True),
    ('FF-FF-AB-CD-EA-BC', True),
    ('12-34-56-78-9A-BG', False)
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

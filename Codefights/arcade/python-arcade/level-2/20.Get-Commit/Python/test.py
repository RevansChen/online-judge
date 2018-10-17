# Python3

from solution1 import getCommit as f

qa = [
    ('0??+0+!!someCommIdhsSt',
     'someCommIdhsSt'),
    ('noAUTHORofTHIScOmMiT',
     'noAUTHORofTHIScOmMiT'),
    ('?????!+0',
     ''),
    ('!0?!++?empThddsEldfeojLEJlfdk',
     'empThddsEldfeojLEJlfdk'),
    ('+?!00+?sdfejdcdfjwlejflsfjDjfejfLDJfodKJDFLJq',
     'sdfejdcdfjwlejflsfjDjfejfLDJfodKJDFLJq')
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

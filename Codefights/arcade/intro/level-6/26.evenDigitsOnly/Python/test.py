# Python3

from solution1 import evenDigitsOnly as f

qa = [
    (248622, True),
    (642386, False),
    (248842, True),
    (1, False),
    (8, True),
    (2462487, False),
    (468402800, True),
    (2468428, True),
    (5468428, False),
    (7468428, False)
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

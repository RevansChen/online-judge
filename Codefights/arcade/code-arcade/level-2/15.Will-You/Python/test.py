# Python3

from solution1 import willYou as f

qa = [
    (True, True, True, False),
    (True, False, True, True),
    (False, False, False, False),
    (False, False, True, True)
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

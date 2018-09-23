# Python3

from solution1 import deleteDigit as f

qa = [
    (152, 52),
    (1001, 101),
    (10, 1),
    (222219, 22229)
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

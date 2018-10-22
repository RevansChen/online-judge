# Python3

from solution1 import wordPower as f

qa = [
    ('hello', 52),
    ('codesignal', 89),
    ('dog', 26),
    ('i', 9),
    ('abdefghijklmnopqrstuvwxyz', 348)
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

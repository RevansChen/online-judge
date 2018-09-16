# Python3

from solution1 import differentSymbolsNaive as f

qa = [
    ('cabca', 3),
    ('aba', 2),
    ('ccccccccccc', 1),
    ('bcaba', 3),
    ('codesignal', 10)
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

# Python3

from solution1 import commonCharacterCount as f

qa = [
    ('aabcc', 'adcaa', 3),
    ('zzzz', 'zzzzzzz', 4),
    ('abca', 'xyzbac', 3),
    ('a', 'b', 0),
    ('a', 'aaa', 1)
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

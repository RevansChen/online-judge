# Python3

from solution1 import isWordPalindrome as f

qa = [
    ('aibohphobia', True),
    ('hehehehehe', False),
    ('toot', True),
    ('codedog', False),
    ('z', True),
    ('ilongpalindrome', False),
    ('abacaba', True),
    ('zz', True),
    ('aaabaaaa', False),
    ('zzzazzazz', False)
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

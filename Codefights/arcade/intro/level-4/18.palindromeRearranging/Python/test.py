# Python3

from solution1 import palindromeRearranging as f

qa = [
    ('aabb', True),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc', False),
    ('abbcabb', True),
    ('zyyzzzzz', True),
    ('z', True),
    ('zaa', True),
    ('abca', False),
    ('abcad', False),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccaaaaaaaaaaaaa', False),
    ('abdhuierf', False)
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

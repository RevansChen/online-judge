# Python3

from solution1 import longestWord as f

qa = [
    ('Ready, steady, go!', 'steady'),
    ('Ready[[[, steady, go!', 'steady'),
    ('ABCd', 'ABCd'),
    ('To be or not to be', 'not'),
    ('You are the best!!!!!!!!!!!! CodeFighter ever!', 'CodeFighter')
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

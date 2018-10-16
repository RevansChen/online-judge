# Python3

from solution1 import permutationCipher as f

qa = [
    ('iamthebest',
     'zabcdefghijklmnopqrstuvwxy',
     'hzlsgdadrs'),
    ('codesignalrocks',
     'ebtyfkudagizxmvcnojqwlsrhp',
     'tvyfjaumezovtij'),
    ('supersecurepassword',
     'felkjmwchynzgobvadtipqrxsu',
     'tpvjdtjlpdjvfttrbdk'),
    ('myprivatestuff',
     'mvdwjsphaqufinryoltxcgkzbe',
     'ibylagmxjtxcss'),
    ('x',
     'abcdefghijklmnopqrstuvwxyz',
     'x')
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

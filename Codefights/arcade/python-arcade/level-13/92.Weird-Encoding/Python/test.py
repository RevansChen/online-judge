# Python3

from solution1 import weirdEncoding as f

qa = [
    ('-_',
     'Q29kZVNpZ25hbA==',
     'CodeSignal'),
    ('-+',
     'RmlnaHQgb24h',
     'Fight on!'),
    ('/+',
     'U29tZSB2ZXJ5IHN0cmFuZ2UgYW5kIGxvbmcgYXR0YWNobWVudD8+Pw==',
     'Some very strange and long attachment???'),
    ('%$',
     'PyE$ISE$IT8hP2Zlc2VmZXNm',
     '?!?!!?!?!?fesefesf'),
    ('+/',
     'MQ==',
     '1')
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

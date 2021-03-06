# Python3

from solution1 import wordsRecognition as f

qa = [
    ('program', 'develop',
     ['agmr', 'delv']),
    ('code', 'fights',
     ['cdeo', 'fghist']),
    ('silent', 'listen',
     ['', '']),
    ('football', 'soccer',
     ['abflt', 'cers']),
    ('nobeautiful', 'boolean',
     ['fitu', ''])
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

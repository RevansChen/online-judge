# Python3

from solution1 import urlSimilarity as f

qa = [
    ('https://codesignal.com/home/test?param1=42&param3=testing&login=admin',
     'https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin',
     19),
    ('https://codesignal.com/home/test?param1=42&param3=testing&login=admin',
     'http://codesignal.org/about?42=param1&tesing=param3&admin=login',
     0),
    ('https://www.google.com/search?q=codesignal',
     'http://www.google.com/search?q=codesignal',
     13),
    ('ftp://www.example.com/query?varName=value',
     'http://example.com/query?varName=value',
     3),
    ('ftp://www',
     'http://anotherexample.com/www?ftp=http',
     0),
    ('https://codesignal.com/home/test?param1=42&param3=testing&login=admin&param4=abc&param5=codesignal',
     'https://codesignal.com/home/secret/test?param3=fish&param1=42&codesignal=admin&param5=test',
     20)
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

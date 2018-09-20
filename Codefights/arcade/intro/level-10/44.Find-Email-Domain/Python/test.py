# Python3

from solution1 import findEmailDomain as f

qa = [
    ('prettyandsimple@example.com',
     'example.com'),
    ('<>[]:,;@\"!#$%&*+-/=?^_{}| ~.a\"@example.org',
     'example.org'),
    ('someaddress@yandex.ru',
     'yandex.ru'),
    ('\" \"@xample.org',
     'xample.org'),
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

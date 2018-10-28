# Python3

from solution1 import cyclicName as f

qa = [
    ('nicecoder', 15,
     'nicecoderniceco'),
    ('codesignal', 50,
     'codesignalcodesignalcodesignalcodesignalcodesignal'),
    ('test', 4,
     'test'),
    ('q', 8,
     'qqqqqqqq'),
    ('ninja', 15,
     'ninjaninjaninja')
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

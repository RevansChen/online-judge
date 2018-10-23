# Python3

from solution1 import createHistogram as f

qa = [
    ('*', [12, 12, 14, 3, 12, 15, 14],
     ['************',
      '************',
      '**************',
      '***',
      '************',
      '***************',
      '**************']),
    ('>', [20],
     ['>>>>>>>>>>>>>>>>>>>>']),
    ('@', [12, 12, 30, 40, 14, 0, 29, 43],
     ['@@@@@@@@@@@@',
      '@@@@@@@@@@@@',
      '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
      '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
      '@@@@@@@@@@@@@@',
      '',
      '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
      '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@']),
    ('$', [14, 43],
     ['$$$$$$$$$$$$$$',
      '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$']),
    ('O', [44, 31, 38],
     ['OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
      'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
      'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'])
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

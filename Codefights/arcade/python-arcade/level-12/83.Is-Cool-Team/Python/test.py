# Python3

from solution1 import isCoolTeam as f

qa = [
    (['Mark',
      'Kelly',
      'Kurt',
      'Terk'],
     True),
    (['Lucy'],
     True),
    (['Rob',
      'Bobby',
      'Billy'],
     False),
    (['Sophie',
      'Boris',
      'EriC',
      'Charlotte'],
     True),
    (['Sophie',
      'Boris',
      'Eric',
      'Charlotte',
      'Charlie'],
     False),
    (['Sophie',
      'Edward',
      'Deb',
      'Boris',
      'Stephanie',
      'Eric',
      'Charlotte',
      'Eric',
      'Charlie'],
     True),
    (['Bobo',
      'obob',
      'Bobo',
      'ob'],
     True),
    (['Edward',
      'Daniel',
      'Lily'],
     True),
    (['ANTONY',
      'James'],
     False),
    (['Ned',
      'Ben'],
     True)
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

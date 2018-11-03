# Python3

from solution1 import checkPassword as f

qa = [
    (['hello',
      'world',
      'I',
      'like',
      'coding'],
     'like', 4),
    (['hello',
      'world',
      'I',
      'like',
      'coding'],
     'qwerty123', -1),
    (['codesignal'],
     'codesignal', 1),
    (['123',
      '456',
      'qwerty',
      'zzz',
      'password',
      'genius239',
      'password'],
     'password', 5),
    (['warrior',
      'ninja',
      'trainee'],
     'recruit', -1),
    ([],
     'igiveup', -1)
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

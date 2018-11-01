# Python3

from solution1 import fibonacciList as f

qa = [
    (6,
     [[],
      [0],
      [0],
      [0, 0],
      [0, 0, 0],
      [0, 0, 0, 0, 0]]),
    (2,
     [[],
      [0]]),
    (3,
     [[],
      [0],
      [0]]),
    (8,
     [[],
      [0],
      [0],
      [0, 0],
      [0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
    (5,
     [[],
      [0],
      [0],
      [0, 0],
      [0, 0, 0]])
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

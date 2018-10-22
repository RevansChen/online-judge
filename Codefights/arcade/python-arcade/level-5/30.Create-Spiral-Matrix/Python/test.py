# Python3

from solution1 import createSpiralMatrix as f

qa = [
    (3,
     [[5, 4, 3],
      [6, 9, 2],
      [7, 8, 1]]),
    (4,
     [[ 7,  6,  5, 4],
      [ 8, 15, 14, 3],
      [ 9, 16, 13, 2],
      [10, 11, 12, 1]]),
    (5,
     [[ 9,  8,  7,  6, 5],
      [10, 21, 20, 19, 4],
      [11, 22, 25, 18, 3],
      [12, 23, 24, 17, 2],
      [13, 14, 15, 16, 1]]),
    (6,
     [[11, 10,  9,  8,  7, 6],
      [12, 27, 26, 25, 24, 5],
      [13, 28, 35, 34, 23, 4],
      [14, 29, 36, 33, 22, 3],
      [15, 30, 31, 32, 21, 2],
      [16, 17, 18, 19, 20, 1]])
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

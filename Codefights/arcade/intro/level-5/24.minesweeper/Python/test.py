# Python3

from solution1 import minesweeper as f

qa = [
    ([[True, False, False],
      [False, True, False],
      [False, False, False]],
     [[1, 2, 1],
      [2, 1, 1],
      [1, 1, 1]]),
    ([[False, False, False],
      [False, False, False]],
     [[0, 0, 0],
      [0, 0, 0]]),
    ( [[True, False, False, True],
      [False, False, True, False],
      [True, True, False, True]],
     [[0, 2, 2, 1],
      [3, 4, 3, 3],
      [1, 2, 3, 1]]),
    ([[True, True, True],
      [True, True, True],
      [True, True, True]],
     [[3, 5, 3],
      [5, 8, 5],
      [3, 5, 3]]),
    ([[False, True, True, False],
      [True, True, False, True],
      [False, False, True, False]],
     [[3, 3, 3, 2],
      [2, 4, 5, 2],
      [2, 3, 2, 2]]),
    ([[True, False],
      [True, False],
      [False, True],
      [False, False],
      [False, False]],
     [[1, 2],
      [2, 3],
      [2, 1],
      [1, 1],
      [0, 0]])
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

# Python3

from solution1 import doodledPassword as f

qa = [
    ([1, 2, 3, 4, 5],
     [[1, 2, 3, 4, 5],
      [2, 3, 4, 5, 1],
      [3, 4, 5, 1, 2],
      [4, 5, 1, 2, 3],
      [5, 1, 2, 3, 4]]),
    ([5],
     [[5]]),
    ([2, 2, 2, 2],
     [[2, 2, 2, 2],
      [2, 2, 2, 2],
      [2, 2, 2, 2],
      [2, 2, 2, 2]]),
    ([9, 8, 7, 5, 4],
     [[9, 8, 7, 5, 4],
      [8, 7, 5, 4, 9],
      [7, 5, 4, 9, 8],
      [5, 4, 9, 8, 7],
      [4, 9, 8, 7, 5]]),
    ([1, 5, 1, 5, 1, 4],
     [[1, 5, 1, 5, 1, 4],
      [5, 1, 5, 1, 4, 1],
      [1, 5, 1, 4, 1, 5],
      [5, 1, 4, 1, 5, 1],
      [1, 4, 1, 5, 1, 5],
      [4, 1, 5, 1, 5, 1]])
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

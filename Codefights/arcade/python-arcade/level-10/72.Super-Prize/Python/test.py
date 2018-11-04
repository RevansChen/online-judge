# Python3

from solution1 import superPrize as f

qa = [
    ([12, 43, 13, 465, 1, 13],
     2, 3,
     [4]),
    ([],
     2, 2,
     []),
    ([988, 126, 876, 615, 323, 835, 815, 2, 867, 952, 95, 397, 546, 762, 350],
     17, 7,
     []),
    ([41, 51, 91, 72, 71, 30, 28, 35, 55, 62, 65, 45, 100, 54, 83, 69, 66, 43],
     2, 5,
     [6, 8, 12]),
    ([64, 67, 86, 87, 69, 49, 47, 75, 43, 74, 23, 47, 77, 83, 67, 24, 11, 59, 19, 88],
     4, 5,
     [8])
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

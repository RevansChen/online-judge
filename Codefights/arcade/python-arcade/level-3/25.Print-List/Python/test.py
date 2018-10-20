# Python3

from solution1 import printList as f

qa = [
    ([1, 2, 3, 4, 5],
     'This is your list: [1, 2, 3, 4, 5]'),
    ([],
     'This is your list: []'),
    ([-74, -71, -7, -88, 13, -22, 7, 7, 71, 28, -78, -17, 77, 10],
     'This is your list: [-74, -71, -7, -88, 13, -22, 7, 7, 71, 28, -78, -17, 77, 10]'),
    ([71],
     'This is your list: [71]'),
    ([58, -93, 20, 3, 37, 29, 94, 60, -55, 19, -57, -24, -89, -21],
     'This is your list: [58, -93, 20, 3, 37, 29, 94, 60, -55, 19, -57, -24, -89, -21]')
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

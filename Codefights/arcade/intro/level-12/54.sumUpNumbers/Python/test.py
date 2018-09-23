# Python3

from solution1 import sumUpNumbers as f

qa = [
    ('2 apples, 12 oranges', 14),
    ('123450', 123450),
    ('Your payment method is invalid', 0),
    ('no digits at all', 0),
    ('there are some (12) digits 5566 in this 770 string 239', 6587)
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

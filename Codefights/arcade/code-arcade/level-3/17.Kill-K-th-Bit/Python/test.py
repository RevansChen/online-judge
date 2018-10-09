# Python3

from solution1 import killKthBit as f

qa = [
    (37, 3, 33),
    (37, 4, 37),
    (37, 2, 37),
    (0, 4, 0),
    (2147483647, 16, 2147450879),
    (374823748, 13, 374819652),
    (2734827, 4, 2734819),
    (1084197039, 15, 1084197039),
    (1160825071, 3, 1160825067),
    (2039063284, 4, 2039063284)
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

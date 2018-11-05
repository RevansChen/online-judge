# Python3

from solution1 import simpleComposition as f

qa = [
    ('math.log10', 'abs', -100, 2),
    ('math.sin', 'math.cos', 34.4, -0.834717445664),
    ('int', 'lambda x: 1.0 * x / 22', 1000, 45),
    ('math.exp', 'lambda x: x ** 0', -1000, 2.71828182846),
    ('lambda z: z', 'lambda y: y', 239, 239)
]

for *q, a in qa:
    for i, e in enumerate(q):
        print('input{0}: {1}'.format(i + 1, e))
    ans = round(f(*q), 6)
    if ans != round(a, 6):
        print('  [failed]')
        print('    output:', ans)
        print('    expected:', a)
    else:
        print('  [ok]')
        print('    output:', ans)
    print()

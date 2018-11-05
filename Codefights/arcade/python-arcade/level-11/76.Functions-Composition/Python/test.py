# Python3

from solution1 import functionsComposition as f

qa = [
    (['abs',
      'math.sin',
      'lambda x: 3 * x / 2'],
     3.1415, 1),
    (['math.sin',
      'math.cos',
      'lambda x: x * 2',
      'lambda x: x ** 2'],
     1, -0.404239153852),
    (['lambda z: z',
      'lambda z: 1.0 * z / 13'],
     -1000, -76.9230769231),
    (['float'],
     1000, 1000),
    (['abs'],
     -20, 20)
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

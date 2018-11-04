# Python3

from solution1 import tryFunctions as f

qa = [
    (1,
     ['math.sin',
      'math.cos',
      'lambda x: x * 2',
      'lambda x: x ** 2'],
     [0.84147, 0.5403, 2, 1]),
    (-20,
     ['abs'],
     [20]),
    (25.5,
     ['lambda x: int(x)',
      'int',
      'math.floor'],
     [25, 25, 25]),
    (3,
     ['math.factorial',
      'math.exp',
      'lambda x: 2 ** x'],
     [6, 20.0855369232, 8]),
    (-1000,
     ['lambda z: z',
      'lambda z: 1.0 * z / 13'],
     [-1000, -76.9230769231])
]

for *q, a in qa:
    for i, e in enumerate(q):
        print('input{0}: {1}'.format(i + 1, e))
    ans = [ round(i, 5) for i in f(*q) ]
    if ans != [ round(i, 5) for i in a ]:
        print('  [failed]')
        print('    output:', ans)
        print('    expected:', a)
    else:
        print('  [ok]')
        print('    output:', ans)
    print()

# Python3

from solution1 import transposeDictionary as f

qa = [
    ({
        'validate': 'py',
        'getLimits': 'md',
        'generateOutputs': 'json'
    },
     [['json', 'generateOutputs'],
      ['md', 'getLimits'],
      ['py', 'validate']]),
    ({
        'styleChecker': 'cpp',
        'autoBugfixes': 'py'
    },
     [['cpp', 'styleChecker'],
      ['py', 'autoBugfixes']]),
    ({},
     []),
    ({'generateTests': 'json'},
     [['json', 'generateTests']]),
    ({
        'runSolutions': 'validate',
        'generateTests': 'generateOutputs',
        'validate': 'runSolutions',
        'generatePeh': 'generateMeh',
        'generateMeh': 'generatePeh',
        'generateOutputs': 'generateTests'
    },
     [['generateMeh', 'generatePeh'],
      ['generateOutputs', 'generateTests'],
      ['generatePeh', 'generateMeh'],
      ['generateTests', 'generateOutputs'],
      ['runSolutions', 'validate'],
      ['validate', 'runSolutions']])
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

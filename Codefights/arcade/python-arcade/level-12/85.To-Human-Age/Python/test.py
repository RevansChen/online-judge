# Python3

from solution1 import toHumanAge as f

qa = [
    ([['cat', '2'],
      ['dog', '2'],
      ['human', '2']],
     ['25 y.o. in human age',
      '24 y.o. in human age',
      '2 y.o. in human age']),
    ([['cat', '1']],
     ['12 y.o. in human age']),
    ([['cat', '20'],
      ['human', '1'],
      ['human', '12'],
      ['cat', '5'],
      ['dog', '10'],
      ['cat', '15'],
      ['dog', '1'],
      ['dog', '17'],
      ['dog', '13'],
      ['cat', '20'],
      ['human', '3'],
      ['dog', '6'],
      ['human', '3'],
      ['dog', '20'],
      ['human', '12'],
      ['human', '4'],
      ['cat', '14'],
      ['dog', '18'],
      ['human', '6'],
      ['dog', '17'],
      ['human', '2'],
      ['cat', '17'],
      ['dog', '18'],
      ['cat', '20'],
      ['dog', '0'],
      ['human', '12'],
      ['dog', '2'],
      ['human', '12'],
      ['dog', '1'],
      ['human', '18'],
      ['dog', '2'],
      ['human', '18'],
      ['cat', '4'],
      ['cat', '5'],
      ['human', '0'],
      ['dog', '0'],
      ['dog', '14'],
      ['human', '15'],
      ['human', '7'],
      ['human', '18'],
      ['cat', '18'],
      ['human', '15'],
      ['dog', '13']],
     ['97 y.o. in human age',
      '1 y.o. in human age',
      '12 y.o. in human age',
      '37 y.o. in human age',
      '56 y.o. in human age',
      '77 y.o. in human age',
      '15 y.o. in human age',
      '84 y.o. in human age',
      '68 y.o. in human age',
      '97 y.o. in human age',
      '3 y.o. in human age',
      '40 y.o. in human age',
      '3 y.o. in human age',
      '96 y.o. in human age',
      '12 y.o. in human age',
      '4 y.o. in human age',
      '73 y.o. in human age',
      '88 y.o. in human age',
      '6 y.o. in human age',
      '84 y.o. in human age',
      '2 y.o. in human age',
      '85 y.o. in human age',
      '88 y.o. in human age',
      '97 y.o. in human age',
      '0 y.o. in human age',
      '12 y.o. in human age',
      '24 y.o. in human age',
      '12 y.o. in human age',
      '15 y.o. in human age',
      '18 y.o. in human age',
      '24 y.o. in human age',
      '18 y.o. in human age',
      '33 y.o. in human age',
      '37 y.o. in human age',
      '0 y.o. in human age',
      '0 y.o. in human age',
      '72 y.o. in human age',
      '15 y.o. in human age',
      '7 y.o. in human age',
      '18 y.o. in human age',
      '89 y.o. in human age',
      '15 y.o. in human age',
      '68 y.o. in human age']),
    ([['human', '9'],
      ['cat', '2'],
      ['dog', '11'],
      ['dog', '14'],
      ['cat', '16'],
      ['cat', '0'],
      ['cat', '8'],
      ['dog', '11'],
      ['cat', '3'],
      ['human', '8']],
     ['9 y.o. in human age',
      '25 y.o. in human age',
      '60 y.o. in human age',
      '72 y.o. in human age',
      '81 y.o. in human age',
      '0 y.o. in human age',
      '49 y.o. in human age',
      '60 y.o. in human age',
      '29 y.o. in human age',
      '8 y.o. in human age']),
    ([['human', '19'],
      ['dog', '6'],
      ['cat', '16'],
      ['dog', '9'],
      ['cat', '7'],
      ['human', '1'],
      ['dog', '10'],
      ['cat', '5'],
      ['cat', '11'],
      ['dog', '17'],
      ['human', '20'],
      ['human', '14'],
      ['cat', '5'],
      ['cat', '7'],
      ['dog', '13']],
     ['19 y.o. in human age',
      '40 y.o. in human age',
      '81 y.o. in human age',
      '52 y.o. in human age',
      '45 y.o. in human age',
      '1 y.o. in human age',
      '56 y.o. in human age',
      '37 y.o. in human age',
      '61 y.o. in human age',
      '84 y.o. in human age',
      '20 y.o. in human age',
      '14 y.o. in human age',
      '37 y.o. in human age',
      '45 y.o. in human age',
      '68 y.o. in human age'])
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

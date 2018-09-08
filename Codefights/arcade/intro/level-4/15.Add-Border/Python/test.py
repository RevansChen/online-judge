# Python3

from solution1 import addBorder as f

qa = [
    (['abc',
      'ded'],
     ['*****',
      '*abc*',
      '*ded*',
      '*****']),
    (['a'],
     ['***',
      '*a*',
      '***']),
    (['aa',
      '**',
      'zz'],
     ['****',
      '*aa*',
      '****',
      '*zz*',
      '****']),
    (['abcde',
      'fghij',
      'klmno',
      'pqrst',
      'uvwxy'],
     ['*******',
      '*abcde*',
      '*fghij*',
      '*klmno*',
      '*pqrst*',
      '*uvwxy*',
      '*******']),
    (['wzy**'],
     ['*******',
      '*wzy***',
      '*******'])
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

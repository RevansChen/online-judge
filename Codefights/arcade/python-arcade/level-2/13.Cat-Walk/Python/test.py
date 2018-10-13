# Python3

from solution1 import catWalk as f

qa = [
    ('def      m   e  gaDifficu     ltFun        ction(x):',
     'def m e gaDifficu ltFun ction(x):'),
    ('      for      i      in         ra   nge(x,   29):',
     'for i in ra nge(x, 29):'),
    ('r e t u r n True',
     'r e t u r n True'),
    ('  re    turn  x    +  y  *     z',
     're turn x + y * z'),
    ('v er si        on = s   ett ings.VE       RSION',
     'v er si on = s ett ings.VE RSION')
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

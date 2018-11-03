# Python3

from solution1 import greetingsGenerator as f

qa = [
    (['Athos',
      'Porthos',
      'Aramis'],
     ['Hello, Athos!',
      'Hello, Porthos!',
      'Hello, Aramis!']),
    (['Fifer',
      'Fiddler',
      'Edmund'],
     ['Hello, Fifer!',
      'Hello, Fiddler!',
      'Hello, Edmund!']),
    ([],
     []),
    (['Dwarf',
      'Doc',
      'Dopey',
      'Bashful',
      'Grumpy',
      'Sneezy',
      'Sleepy',
      'Happy'],
     ['Hello, Dwarf!',
      'Hello, Doc!',
      'Hello, Dopey!',
      'Hello, Bashful!',
      'Hello, Grumpy!',
      'Hello, Sneezy!',
      'Hello, Sleepy!',
      'Hello, Happy!']),
    (['Hero'],
     ['Hello, Hero!'])
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

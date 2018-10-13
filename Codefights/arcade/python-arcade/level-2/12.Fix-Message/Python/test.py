# Python3

from solution1 import fixMessage as f

qa = [
    ("you'll NEVER believe what that 'FrIeNd' of mine did!!1",
     "You'll never believe what that 'friend' of mine did!!1"),
    ('i',
     'I'),
    ('We are so doomed.',
     'We are so doomed.'),
    ("LOL you've GOT to hear this one XDD",
     "Lol you've got to hear this one xdd"),
    ("ok, here's the TRUTH: I have AbSoLuTeLy NOTHING to do with it!",
     "Ok, here's the truth: i have absolutely nothing to do with it!"),
    (':)',
     ':)')
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

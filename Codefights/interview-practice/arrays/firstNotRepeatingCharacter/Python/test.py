# Python3

from solution1 import firstNotRepeatingCharacter as f

qa = [
    ('abacabad', 'c'),
    ('abacabaabacaba', '_'),
    ('z', 'z'),
    ('bcb', 'c'),
    ('bcccccccb', '_'),
    ('abcdefghijklmnopqrstuvwxyziflskecznslkjfabe', 'd'),
    ('zzz', '_'),
    ('bcccccccccccccyb', 'y'),
    ('xdnxxlvupzuwgigeqjggosgljuhliybkjpibyatofcjbfxwtalc', 'd'),
    ('ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof', 'g')
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

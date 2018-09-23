# Python3

from solution1 import lineEncoding as f

qa = [
    ('aabbbc', '2a3bc'),
    ('abbcabb', 'a2bca2b'),
    ('abcd', 'abcd'),
    ('zzzz', '4z'),
    ('wwwwwwwawwwwwww', '7wa7w'),
    ('ccccccccccccccc', '15c'),
    ('qwertyuioplkjhg', 'qwertyuioplkjhg'),
    ('ssiiggkooo', '2s2i2gk3o'),
    ('adfaaa', 'adf3a'),
    ('bbjaadlkjdl', '2bj2adlkjdl')
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

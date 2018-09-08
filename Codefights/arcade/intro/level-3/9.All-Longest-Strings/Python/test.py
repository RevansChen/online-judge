# Python3

from solution1 import allLongestStrings as f

qa = [
    (["aba", "aa", "ad", "vcd", "aba"],
     ["aba", "vcd", "aba"]),
    (["aa"],
     ["aa"]),
    (["abc", "eeee", "abcd", "dcd"],
     ["eeee", "abcd"]),
    (["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"],
     ["zzzzzz", "abcdef", "aaaaaa"])
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

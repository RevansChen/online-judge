# Python3

from solution2 import maliciousProgram as f

qa = [
    ('01 Jul 2016 16:53:24',
     [2, 3, -1, 0, 5, 4],
     '03 Oct 2015 16:58:28'),
    ('15 Mar 1998 12:09:59',
     [-2, 0, 9, 1, 3, 1],
     '15 Mar 1998 12:09:59'),
    ('28 Jan 1900 16:09:10',
     [1, 1, 0, 5, 10, 15],
     '28 Jan 1900 16:09:10'),
    ('01 Jun 2054 16:02:57',
     [28, -4, 2, 0, 0, 0],
     '29 Feb 2056 16:02:57'),
    ('23 Mar 2045 18:10:20',
     [21, 6, 60, -16, -23, 16],
     '23 Mar 2045 18:10:20'),
    ('01 Jan 1900 00:00:00',
     [30, 11, 100, 23, 59, 59],
     '31 Dec 2000 23:59:59'),
    ('06 May 1999 10:22:18',
     [11, -4, 64, 4, -4, -2],
     '17 Jan 2063 14:18:16'),
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

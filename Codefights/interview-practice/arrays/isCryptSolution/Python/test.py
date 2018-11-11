# Python3

from solution1 import isCryptSolution as f

qa = [
    (["SEND", "MORE", "MONEY"], 
     [["O","0"], 
      ["M","1"], 
      ["Y","2"], 
      ["E","5"], 
      ["N","6"], 
      ["D","7"], 
      ["R","8"], 
      ["S","9"]],
     True),
    (["TEN", "TWO", "ONE"],
     [["O","1"], 
      ["T","0"], 
      ["W","9"], 
      ["E","5"], 
      ["N","4"]],
     False),
    (["ONE", "ONE", "TWO"],
     [["O","2"], 
      ["T","4"], 
      ["W","6"], 
      ["E","1"], 
      ["N","3"]],
     True),
    (["ONE", "ONE", "TWO"],
     [["O","0"], 
      ["T","1"], 
      ["W","2"], 
      ["E","5"], 
      ["N","6"]],
     False),
    (["A", "A", "A"],
     [["A","0"]],
     True),
    (["A", "B", "C"],
     [["A","5"], 
      ["B","6"], 
      ["C","1"]],
     False),
    (["AA", "AA", "AA"], 
     [["A","0"]],
     False),
    (["A", "A", "A"],
     [["A","1"]],
     False),
    (["AA", "AA", "BB"],
     [["A","1"], 
      ["B","2"]],
     True),
    (["BAA", "CAB", "DAB"],
     [["A","0"], 
      ["B","1"], 
      ["C","2"], 
      ["D","4"]],
     False)
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

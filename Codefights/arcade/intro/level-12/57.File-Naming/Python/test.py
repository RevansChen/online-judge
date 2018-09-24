# Python3

from solution1 import fileNaming as f

qa = [
    (["doc",
      "doc",
      "image",
      "doc(1)",
      "doc"],
     ["doc",
      "doc(1)",
      "image",
      "doc(1)(1)",
      "doc(2)"]),
    (["a(1)",
      "a(6)",
      "a",
      "a",
      "a",
      "a",
      "a",
      "a",
      "a",
      "a",
      "a",
      "a"],
     ["a(1)",
      "a(6)",
      "a",
      "a(2)",
      "a(3)",
      "a(4)",
      "a(5)",
      "a(7)",
      "a(8)",
      "a(9)",
      "a(10)",
      "a(11)"]),
    (["dd",
      "dd(1)",
      "dd(2)",
      "dd",
      "dd(1)",
      "dd(1)(2)",
      "dd(1)(1)",
      "dd",
      "dd(1)"],
     ["dd",
      "dd(1)",
      "dd(2)",
      "dd(3)",
      "dd(1)(1)",
      "dd(1)(2)",
      "dd(1)(1)(1)",
      "dd(4)",
      "dd(1)(3)"])
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

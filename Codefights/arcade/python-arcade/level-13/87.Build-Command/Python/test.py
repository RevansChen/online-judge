# Python3

from solution1 import buildCommand as f

qa = [
    ('{"version": "0.1.0","command": "c:python","args": ["app.py"],"problemMatcher": {"fileLocation": ["relative", "${workspaceRoot}"],"pattern": {"regexp": "^(.*)+s$", "message": 1}}}',
     '{"version": "", "command": "", "args": [], "problemMatcher": {"fileLocation": [], "pattern": {"regexp": "", "message": 0}}}'),
    ('{}',
     '{}'),
    ('{"one": "1", "two": [2], "three": 3, "four": 4.6}',
     '{"one": "", "two": [], "three": 0, "four": 0}'),
    ('{"colorsArray":[{"colorName":"red","hexValue":"f00"},{"colorName":"green","hexValue":"0f0"},{"colorName":"blue","hexValue":"00f"},{"colorName":"cyan","hexValue":"0ff"},{"colorName":"magenta","hexValue":"f0f"},{"colorName":"yellow","hexValue":"ff0"},{"colorName":"black","hexValue":"000"}]}',
     '{"colorsArray": []}')
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

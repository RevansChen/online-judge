# Python3

from solution1 import pageComplexity as f

qa = [
    ('<!DOCTYPE html><html>  <body>    <h1>The best heading ever</h1>    <p>The worst paragraph ever.</p>  </body></html>',
     ['h1', 'p']),
    ("<!DOCTYPE html><html>  <body>    <h1>The best heading ever</h1>    <!--Actually it isn't, but if you can use it if you want >_< -->    <p>The worst paragraph ever.</p>  </body></html>",
     ['h1', 'p']),
    ('<!DOCTYPE html><html><body><h1>This is first heading 1</h1><h2>This is second heading 2</h2><h3>This is third heading 3</h3><h4>This is another heading</h4><h5>This is just heading...</h5><h6>Oh I really got tired of calculating</h6></body></html>',
     ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']),
    ('<!DOCTYPE html><html><body><h2>Polular russian drinks</h2><ul>  <li>Coffee</li>  <li>Tea    <ul>    <li>Black tea</li>    <li>Green tea      <ul>      <li>China</li>      <li>Africa</li>      </ul>    </li>    </ul>  </li>  <li>Milk</li>  <li>Vodka</li>  <li>Vodka</li>  <li>Vodka</li>  <li>Vodka</li></ul></body></html>',
     ['li']),
    ('<!DOCTYPE html><html><body><h1 style=\"text-align:center;\">Centered Heading</h1><p style=\"text-align:center;\">Centered paragraph.</p></body></html>',
     ['h1', 'p'])
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

# Python - 3.6.0

Test.it('Example tests')
Test.assert_equals(last_digit(4, 1), 4)
Test.assert_equals(last_digit(4, 2), 6)
Test.assert_equals(last_digit(9, 7), 9)
Test.assert_equals(last_digit(10, 10 ** 10), 0)
Test.assert_equals(last_digit(2 ** 200, 2 ** 300), 6)
Test.assert_equals(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)

Test.it('x ** 0')
for nmbr in range(1, 9):
    a = nmbr ** nmbr
    Test.it('Testing %d and %d' % (a, 0))
    Test.assert_equals(last_digit(a, 0), 1, 'x ** 0 must return 1')

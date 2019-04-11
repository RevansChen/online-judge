# Python - 3.6.0

test.it('Should work for sample test cases.')
test.assert_equals(replace_dots(''), '')
test.assert_equals(replace_dots('no dots'), 'no dots')
test.assert_equals(replace_dots('one.two.three'), 'one-two-three')
test.assert_equals(replace_dots('........'), '--------')

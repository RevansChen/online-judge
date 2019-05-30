# Python - 3.6.0

Test.describe('Sample Test')
Test.it('Single Digit Number')
test.assert_equals(jumping_number(1), 'Jumping!!')
test.assert_equals(jumping_number(7), 'Jumping!!')
test.assert_equals(jumping_number(9), 'Jumping!!')

Test.it('Two Digit Number')
test.assert_equals(jumping_number(23), 'Jumping!!')
test.assert_equals(jumping_number(32), 'Jumping!!')
test.assert_equals(jumping_number(79), 'Not!!')
test.assert_equals(jumping_number(98), 'Jumping!!')

Test.it('Larger Numbers')
test.assert_equals(jumping_number(8987), 'Jumping!!')
test.assert_equals(jumping_number(4343456), 'Jumping!!')
test.assert_equals(jumping_number(98789876), 'Jumping!!')

# Python - 3.6.0

Test.describe('Basic Tests')
Test.it('should pass basic tests')
Test.assert_equals(is_divide_by(-12, 2, -6), True)
Test.assert_equals(is_divide_by(-12, 2, -5), False)
Test.assert_equals(is_divide_by(45, 1, 6), False)
Test.assert_equals(is_divide_by(45, 5, 15), True)
Test.assert_equals(is_divide_by(4, 1, 4), True)
Test.assert_equals(is_divide_by(15, -5, 3), True)

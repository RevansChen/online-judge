# Python - 3.6.0

Test.describe('Basic tests')
Test.it('should return correct for Normal Values')
Test.assert_equals(find_digit(5673, 4), 5)
Test.assert_equals(find_digit(129, 2), 2)
Test.assert_equals(find_digit(-2825, 3), 8)
Test.assert_equals(find_digit(0, 20), 0)
Test.assert_equals(find_digit(65, 0), -1)
Test.assert_equals(find_digit(24, -8), -1)

Test.it('should return correctly for Negative Values')
Test.assert_equals(find_digit(-1234, 2), 3)
Test.assert_equals(find_digit(-5540, 1), 0)

Test.it('should return correctly when Nth is not Positive')
Test.assert_equals(find_digit(678998, 0), -1)
Test.assert_equals(find_digit(-67854, -57), -1)
Test.assert_equals(find_digit(0, -3), -1)

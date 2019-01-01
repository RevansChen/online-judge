# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]), 6)
Test.assert_equals(first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]), None)
Test.assert_equals(first_non_consecutive([4, 6, 7, 8, 9, 11]), 6)
Test.assert_equals(first_non_consecutive([4, 5, 6, 7, 8, 9, 11]), 11)
Test.assert_equals(first_non_consecutive([31, 32]), None)
Test.assert_equals(first_non_consecutive([-3, -2, 0, 1]), 0)
Test.assert_equals(first_non_consecutive([-5, -4, -3, -1]), -1)

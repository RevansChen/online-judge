# Python - 2.7.6

Test.describe('Fixed tests')
Test.assert_equals(divisible_by([1, 2, 3, 4, 5, 6], 2), [2, 4, 6])
Test.assert_equals(divisible_by([1, 2, 3, 4, 5, 6], 3), [3, 6])
Test.assert_equals(divisible_by([0, 1, 2, 3, 4, 5, 6], 4), [0, 4])
Test.assert_equals(divisible_by([0], 4), [0])
Test.assert_equals(divisible_by([1, 3, 5], 2), [])

# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(sort_by_value_and_index([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
Test.assert_equals(sort_by_value_and_index([23, 2, 3, 4, 5]), [2, 3, 4, 23, 5])
Test.assert_equals(sort_by_value_and_index([26, 2, 3, 4, 5]), [2, 3, 4, 5, 26])
Test.assert_equals(sort_by_value_and_index([9, 5, 1, 4, 3]), [1, 9, 5, 3, 4])

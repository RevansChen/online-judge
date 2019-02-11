# Python - 3.6.0

data = [1, 2, 3, 4, 5]

Test.assert_equals(rotate(data, 1), [5, 1, 2, 3, 4], "'n' is 1")
Test.assert_equals(rotate(data, 2), [4, 5, 1, 2, 3], "'n' is 2")
Test.assert_equals(rotate(data, 3), [3, 4, 5, 1, 2], "'n' is 3")
Test.assert_equals(rotate(data, 4), [2, 3, 4, 5, 1], "'n' is 4")
Test.assert_equals(rotate(data, 5), [1, 2, 3, 4, 5], "'n' is 5")

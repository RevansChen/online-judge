# Python - 2.7.6

Test.assert_equals(next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)
Test.assert_equals(next_id([5, 4, 3, 2, 1]), 0)
Test.assert_equals(next_id([0, 1, 2, 3, 5]), 4)
Test.assert_equals(next_id([0, 0, 0, 0, 0, 0]), 1)
Test.assert_equals(next_id([]), 0)

# Python - 2.7.6

Test.describe('Basic Tests')
Test.assert_equals(my_first_kata(3, 5), (3 % 5 + 5 % 3))
Test.assert_equals(my_first_kata('hello', 3), False)
Test.assert_equals(my_first_kata(67, 'bye'), False)
Test.assert_equals(my_first_kata(True, True), False)
Test.assert_equals(my_first_kata(314, 107), (107 % 314 + 314 % 107))
Test.assert_equals(my_first_kata(1, 32), (1 % 32 + 32 % 1))
Test.assert_equals(my_first_kata(-1, -1), (-1 % -1 + -1 % -1))
Test.assert_equals(my_first_kata(19483, 9), (9 % 19483 + 19483 % 9))
Test.assert_equals(my_first_kata('hello', {}), False)
Test.assert_equals(my_first_kata([], 'pippi'), False)

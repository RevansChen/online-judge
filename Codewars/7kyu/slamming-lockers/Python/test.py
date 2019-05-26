# Python - 2.7.6

test.assert_equals(locker_run(1), [1])
test.assert_equals(locker_run(2), [1])
test.assert_equals(locker_run(3), [1])
test.assert_equals(locker_run(5), [1, 4])
test.assert_equals(locker_run(8), [1, 4])
test.assert_equals(locker_run(10), [1, 4, 9])
test.assert_equals(locker_run(20), [1, 4, 9, 16])
test.assert_equals(locker_run(50), [1, 4, 9, 16, 25, 36, 49])
test.assert_equals(locker_run(100), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
test.assert_equals(locker_run(500), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484])

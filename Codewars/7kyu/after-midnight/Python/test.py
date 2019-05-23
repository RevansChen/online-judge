# Python - 2.7.6

Test.describe('Initial Tests')
Test.assert_equals(day_and_time(0), 'Sunday 00:00')
Test.assert_equals(day_and_time(-3), 'Saturday 23:57')
Test.assert_equals(day_and_time(45), 'Sunday 00:45')
Test.assert_equals(day_and_time(759), 'Sunday 12:39')
Test.assert_equals(day_and_time(1236), 'Sunday 20:36')
Test.assert_equals(day_and_time(1447), 'Monday 00:07')
Test.assert_equals(day_and_time(7832), 'Friday 10:32')
Test.assert_equals(day_and_time(18876), 'Saturday 02:36')
Test.assert_equals(day_and_time(259180), 'Thursday 23:40')
Test.assert_equals(day_and_time(-349000), 'Tuesday 15:20')

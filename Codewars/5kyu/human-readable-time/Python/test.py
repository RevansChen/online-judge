# Python - 3.6.0

Test.assert_equals(make_readable(0), '00:00:00')
Test.assert_equals(make_readable(5), '00:00:05')
Test.assert_equals(make_readable(60), '00:01:00')
Test.assert_equals(make_readable(86399), '23:59:59')
Test.assert_equals(make_readable(359999), '99:59:59')

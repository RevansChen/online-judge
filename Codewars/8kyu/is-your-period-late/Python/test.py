# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28), True)
Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
Test.assert_equals(period_is_late(date(2016, 6, 13), date(2016, 6, 29), 28), False)
Test.assert_equals(period_is_late(date(2016, 7, 12), date(2016, 8, 9), 28), False)
Test.assert_equals(period_is_late(date(2016, 7, 12), date(2016, 8, 10), 28), True)
Test.assert_equals(period_is_late(date(2016, 7, 1), date(2016, 8, 1), 30), True)
Test.assert_equals(period_is_late(date(2016, 6, 1), date(2016, 6, 30), 30), False)
Test.assert_equals(period_is_late(date(2016, 1, 1), date(2016, 1, 31), 30), False)
Test.assert_equals(period_is_late(date(2016, 1, 1), date(2016, 2, 1), 30), True)

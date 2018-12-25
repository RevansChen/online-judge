# Python - 2.7.6

Test.describe('Basic tests')
Test.assert_equals(year_days(0), '0 has 366 days')
Test.assert_equals(year_days(-64), '-64 has 366 days')
Test.assert_equals(year_days(2016), '2016 has 366 days')
Test.assert_equals(year_days(1974), '1974 has 365 days')
Test.assert_equals(year_days(-10), '-10 has 365 days')
Test.assert_equals(year_days(666), '666 has 365 days')
Test.assert_equals(year_days(1857), '1857 has 365 days')
Test.assert_equals(year_days(2000), '2000 has 366 days')
Test.assert_equals(year_days(-300), '-300 has 365 days')
Test.assert_equals(year_days(-1), '-1 has 365 days')

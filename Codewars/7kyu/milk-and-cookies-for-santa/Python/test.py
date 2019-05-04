# Python - 3.6.0

from datetime import date

Test.assert_equals(time_for_milk_and_cookies(date(2013, 12, 24)), True)
Test.assert_equals(time_for_milk_and_cookies(date(2013, 10, 24)), False)
Test.assert_equals(time_for_milk_and_cookies(date(3000, 12, 24)), True)

# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(bonus_time(10000, True), '$100000')
Test.assert_equals(bonus_time(25000, True), '$250000')
Test.assert_equals(bonus_time(10000, False), '$10000')
Test.assert_equals(bonus_time(60000, False), '$60000')
Test.assert_equals(bonus_time(2, True), '$20')
Test.assert_equals(bonus_time(78, False), '$78')
Test.assert_equals(bonus_time(67890, True), '$678900')

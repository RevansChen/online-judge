# Python - 3.6.0

Test.describe('two_decimal_places')

Test.it('works for some examples')
Test.assert_equals(two_decimal_places(4.659725356), 4.66, "didn't work for 4.659725356")
Test.assert_equals(two_decimal_places(173735326.3783732637948948), 173735326.38, "didn't work for 173735326.3783732637948948")
Test.assert_equals(two_decimal_places(4.653725356), 4.65, "didn't work for 4.653725356")

# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(calculate_age(2012, 2016), 'You are 4 years old.')
Test.assert_equals(calculate_age(1989, 2016), 'You are 27 years old.')
Test.assert_equals(calculate_age(2000, 2090), 'You are 90 years old.')
Test.assert_equals(calculate_age(2000, 1990), 'You will be born in 10 years.')
Test.assert_equals(calculate_age(2000, 2000), 'You were born this very year!')
Test.assert_equals(calculate_age(900, 2900), 'You are 2000 years old.')
Test.assert_equals(calculate_age(2010, 1990), 'You will be born in 20 years.')
Test.assert_equals(calculate_age(2010, 1500), 'You will be born in 510 years.')
Test.assert_equals(calculate_age(2011, 2012), 'You are 1 year old.')
Test.assert_equals(calculate_age(2000, 1999), 'You will be born in 1 year.')

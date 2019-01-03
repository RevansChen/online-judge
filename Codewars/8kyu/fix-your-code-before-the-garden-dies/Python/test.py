# Python - 2.7.6

Test.describe('Basic tests')
Test.assert_equals(rain_amount(100), 'Your plant has had more than enough water for today!')
Test.assert_equals(rain_amount(40), 'Your plant has had more than enough water for today!')
Test.assert_equals(rain_amount(39), 'You need to give your plant 1mm of water')
Test.assert_equals(rain_amount(5), 'You need to give your plant 35mm of water')
Test.assert_equals(rain_amount(0), 'You need to give your plant 40mm of water')

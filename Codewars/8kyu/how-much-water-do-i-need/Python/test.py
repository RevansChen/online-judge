# Python - 3.6.0

Test.describe('static tests')
Test.it('Should work for static tests')
Test.assert_equals(how_much_water(10, 10, 21), 'Too much clothes', '')
Test.assert_equals(how_much_water(10, 10, 2), 'Not enough clothes', '')
Test.assert_equals(how_much_water(10, 11, 20), 23.58, '')
Test.assert_equals(how_much_water(50, 15, 29), 189.87, '')

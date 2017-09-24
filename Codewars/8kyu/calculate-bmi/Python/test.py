# Python - 3.4.3

Test.describe('Basic tests')
Test.assert_equals(bmi(50, 1.80), 'Underweight')
Test.assert_equals(bmi(80, 1.80), 'Normal')
Test.assert_equals(bmi(90, 1.80), 'Overweight')
Test.assert_equals(bmi(110, 1.80), 'Obese')
Test.assert_equals(bmi(50, 1.50), 'Normal')

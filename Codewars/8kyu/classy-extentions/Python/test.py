# Python - 2.7.6

Test.describe('Fixed Tests')
cat = Cat('Mr Whiskers')
Test.assert_equals(cat.speak(), 'Mr Whiskers meows.')
cat = Cat('Lamp')
Test.assert_equals(cat.speak(), 'Lamp meows.')
cat = Cat('$$Money Bags$$')
Test.assert_equals(cat.speak(), '$$Money Bags$$ meows.')

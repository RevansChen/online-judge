# Python - 2.7.6

print 'Can you make newly created dogs bark?'
apollo = Dog('Apollo', 'Dobermann', 'male', '4')
zeus = Dog('Zeus', 'Dobermann', 'male', '4')

Test.assert_equals(apollo.bark(), 'Woof!')
Test.assert_equals(zeus.bark(), 'Woof!')

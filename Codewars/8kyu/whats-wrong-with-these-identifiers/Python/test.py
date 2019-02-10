# Python - 3.6.0

Test.describe('Tests')
Test.it('should be defined')
Test.expect(Person, 'Person is not defined')

Test.it('should have at least 4 properties')
Test.assert_equals(len(Person.keys()), 4, 'Person does not have 4 properties')

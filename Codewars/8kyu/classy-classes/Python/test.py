# Python - 3.6.0

Test.describe('Basic tests')
names = ['john', 'matt', 'alex', 'cam']
ages = [16, 25, 57, 39]
for name, age in zip(names, ages):
    person = Person(name, age)
    Test.it(f'Testing for {name} and {age}')
    Test.assert_equals(person.info, f'{name}s age is {age}')

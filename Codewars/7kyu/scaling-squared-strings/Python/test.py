# Python - 3.6.0

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('scale')
Test.it('Basic tests')
a = 'abcd\nefgh\nijkl\nmnop'
r = 'aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp'
testing(scale(a, 2, 3), r)
testing(scale('', 5, 5), '')
testing(scale('Kj\nSH', 1, 2), 'Kj\nKj\nSH\nSH')

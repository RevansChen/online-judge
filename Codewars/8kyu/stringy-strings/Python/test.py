# Python - 2.7.6

test.describe('Basic Tests')

test.it('Should be a string')
test.assert_equals(str(type(stringy(5)))[1:-1], "type 'str'", "stringy() should return a string")

test.it("Should start with '1'")
test.assert_equals(stringy(10)[0], '1', "Whoops your string doesn't start with a '1'")

test.it('Should have the correct length')
for i in xrange(1, 5):
    test.assert_equals(len(stringy(i)), i, 'Make sure your string is the right length')

test.it('Should work for some simple tests')
test.assert_equals(stringy(3), '101', 'oops try again')
test.assert_equals(stringy(5), '10101', 'oops try again')
test.assert_equals(stringy(12), '101010101010', 'oops try again')
test.assert_equals(stringy(26), '10101010101010101010101010', 'oops try again')
test.assert_equals(stringy(28), '1010101010101010101010101010', 'oops try again')

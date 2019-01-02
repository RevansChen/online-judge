# Python - 2.7.6

Test.describe('Basic tests')
Test.it('Correct guess should return true')
guesser = Guesser(10, 2)
guesser.guess(10)
guesser.guess(10)
guesser.guess(10)
guesser.guess(10)
Test.assert_equals(guesser.guess(10), True)

Test.it('Wrong guess should return false')
guesser = Guesser(10, 2)
guesser.guess(1)
Test.assert_equals(guesser.guess(1), False)

Test.it('Lives ran out should throw')
guesser = Guesser(10, 2)
guesser.guess(1)
guesser.guess(2)

Test.expect_error('Expect error: "Omae wa mo shindeiru"', lambda: guesser.guess(10))

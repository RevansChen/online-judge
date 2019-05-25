# Python - 3.6.0

@test.describe('Sample Tests')
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_tests():
        test.assert_equals(last([1, 2, 3]), 3, 'last([1, 2, 3]) == 3')
        test.assert_equals(last([]), None, 'last([]) == None')

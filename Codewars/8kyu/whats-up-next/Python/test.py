# Python - 3.6.0

@test.describe('next_item')
def test_next_item():
    @test.it('should pass some tests')
    def tests():
        Test.assert_equals(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5), 6)
        Test.assert_equals(next_item(['a', 'b', 'c'], 'd'), None)
        Test.assert_equals(next_item(['a', 'b', 'c'], 'c'), None)
        Test.assert_equals(next_item('testing', 't'), 'e')
        Test.assert_equals(next_item(iter(range(1, 30000)), 12), 13)

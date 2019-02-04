# Python - 3.6.0

@test.describe('elevator(left, right, call)')
def elevator_test():
    @test.it('should work for the examples provided in the Kata description')
    def sample_tests():
        test.assert_equals(elevator(0, 1, 0), 'left')
        test.assert_equals(elevator(0, 1, 1), 'right')
        test.assert_equals(elevator(0, 1, 2), 'right')
        test.assert_equals(elevator(0, 0, 0), 'right')
        test.assert_equals(elevator(0, 2, 1), 'right')

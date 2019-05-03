# Python - 3.6.0

@test.describe('Basic Tests')
def basic_tests():
    @test.it('should return true for -0.0 and false for all other numbers')
    def basic_test_case():
        test.assert_equals(is_negative_zero(-0.0), True)
        test.assert_equals(is_negative_zero(-(float('inf'))), False)
        test.assert_equals(is_negative_zero(-5.0), False)
        test.assert_equals(is_negative_zero(-4.0), False)
        test.assert_equals(is_negative_zero(-3.0), False)
        test.assert_equals(is_negative_zero(-2.0), False)
        test.assert_equals(is_negative_zero(-1.0), False)
        test.assert_equals(is_negative_zero(0.0), False)
        test.assert_equals(is_negative_zero(1.0), False)
        test.assert_equals(is_negative_zero(2.0), False)
        test.assert_equals(is_negative_zero(3.0), False)
        test.assert_equals(is_negative_zero(4.0), False)
        test.assert_equals(is_negative_zero(5.0), False)
        test.assert_equals(is_negative_zero(float('inf')), False)

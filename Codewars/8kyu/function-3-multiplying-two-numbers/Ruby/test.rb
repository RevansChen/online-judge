# Ruby - MRI 2.3.0

Test.describe "Solution" do
    Test.it "sample tests" do
        Test.assert_equals(multiply(0, 1), 0)
        Test.assert_equals(multiply(1, 1), 1)
        Test.assert_equals(multiply(2, 2), 4)
        Test.assert_equals(multiply(3, 3), 9)
        Test.assert_equals(multiply(4, 3), 12)
        Test.assert_equals(multiply(5, 3), 15)
        Test.assert_equals(multiply(10, 8), 80)
        Test.assert_equals(multiply(10, 10), 100)
        Test.assert_equals(multiply(10, -10), -100)
        Test.assert_equals(multiply(-10, 10), -100)
        Test.assert_equals(multiply(-10, -10), 100)
        Test.assert_equals(multiply(20, 10), 200)
    end
end
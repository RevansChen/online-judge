describe "Solution" do
    it "sample tests" do
        Test.assert_equals(solution(1), "I")
        Test.assert_equals(solution(4), "IV")
        Test.assert_equals(solution(6), "VI")
        Test.assert_equals(solution(182), "CLXXXII")
        Test.assert_equals(solution(1990), "MCMXC")
        Test.assert_equals(solution(1875), "MDCCCLXXV")
        Test.assert_equals(solution(2008), "MMVIII")
        Test.assert_equals(solution(1666), "MDCLXVI")
        Test.assert_equals(solution(1000), "M")
        Test.assert_equals(solution(2007), "MMVII")
    end
end
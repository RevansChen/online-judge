// C++ - 14

Describe(Kata) {
    It(Fixed_Test) {
        Assert::That(solution(1), Equals("I"));
        Assert::That(solution(4), Equals("IV"));
        Assert::That(solution(6), Equals("VI"));
        Assert::That(solution(182), Equals("CLXXXII"));
        Assert::That(solution(1990), Equals("MCMXC"));
        Assert::That(solution(1875), Equals("MDCCCLXXV"));
        Assert::That(solution(2008), Equals("MMVIII"));
        Assert::That(solution(1666), Equals("MDCLXVI"));
        Assert::That(solution(1000), Equals("M"));
        Assert::That(solution(2007), Equals("MMVII"));
    }
};

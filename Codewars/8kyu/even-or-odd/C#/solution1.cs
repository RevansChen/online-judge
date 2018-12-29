// C# - 7.3

using System;

namespace Solution {
    public class SolutionClass {
        public static string EvenOrOdd(int number) =>
            (((number & 1) == 1) ? "Odd" : "Even");
    }
}

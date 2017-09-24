// C# - Mono 4.2.3

using NUnit.Framework;
using System;

namespace Solution {
    [TestFixture]
    public class SolutionTest {
        private static object[] testCases = new object[] {
            new object[] {0, 1, 0},
            new object[] {1, 1, 1},
            new object[] {2, 2, 4},
            new object[] {3, 3, 9},
            new object[] {4, 3, 12},
            new object[] {5, 3, 15},
            new object[] {10, 8, 80},
            new object[] {10, 10, 100},
            new object[] {10, -10, -100},
            new object[] {-10, 10, -100},
            new object[] {-10, -10, 100},
            new object[] {20, 10, 200}
        };

        [Test, TestCaseSource("testCases")]
        public void SampleTest(int a, int b, int expected) {
            Assert.AreEqual(expected, Kata.Multiply(a, b));
        }
    }
}
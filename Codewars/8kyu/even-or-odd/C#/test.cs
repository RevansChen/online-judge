// C# - 7.3

using System;
using NUnit.Framework;

namespace Solution {
    [TestFixture]
    public class SolutionTest {
        [Test]
        public void MyTest() {
            Assert.AreEqual("Even", SolutionClass.EvenOrOdd(2));
            Assert.AreEqual("Odd", SolutionClass.EvenOrOdd(1));
            Assert.AreEqual("Even", SolutionClass.EvenOrOdd(0));
            Assert.AreEqual("Odd", SolutionClass.EvenOrOdd(7));
            Assert.AreEqual("Odd", SolutionClass.EvenOrOdd(-1));
        }
    }
}

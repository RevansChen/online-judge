// C# - 7.3

namespace Solution {
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class KataTests {
        [Test]
        public void BasicTest() {
            Assert.AreEqual(true, Kata.All(new int[] { 1, 2, 3, 4, 5 }, v => v < 9));
            Assert.AreEqual(false, Kata.All(new int[] { 1, 2, 3, 4, 5 }, v => v > 9));
        }
    }
}

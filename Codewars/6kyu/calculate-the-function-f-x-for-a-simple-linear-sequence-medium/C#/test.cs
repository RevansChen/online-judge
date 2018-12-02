// C# - Mono 4.2.3

using System;
using NUnit.Framework;

[TestFixture]
public class CodeWarsTest {
    [Test]
    public void Test1() {
        Assert.IsTrue(Kata.GetFunction(new[] { 0, 1, 2, 3, 4 })(5) == 5);
    }

    [Test]
    public void Test2() {
        Assert.IsTrue(Kata.GetFunction(new[] { 0, 3, 6, 9, 12 })(10) == 30);
    }

    [Test]
    [ExpectedException(typeof(ArgumentException))]
    public void ShouldFail() {
        Kata.GetFunction(new[] { 0, 1, 2, 3, 10 })(5);
    }
}

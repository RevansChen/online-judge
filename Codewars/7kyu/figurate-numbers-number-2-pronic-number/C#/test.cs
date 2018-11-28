// C# - 7.3

using NUnit.Framework;
using System;

[TestFixture]
public class Test {
    [Test]
    public static void FixedTest() {
        Assert.AreEqual(true, Kata.IsPronic(0));
        Assert.AreEqual(false, Kata.IsPronic(1));
        Assert.AreEqual(true, Kata.IsPronic(2));
        Assert.AreEqual(false, Kata.IsPronic(3));
        Assert.AreEqual(false, Kata.IsPronic(4));
        Assert.AreEqual(false, Kata.IsPronic(5));
        Assert.AreEqual(true, Kata.IsPronic(6));
        Assert.AreEqual(false, Kata.IsPronic(-3));
        Assert.AreEqual(false, Kata.IsPronic(-27));
    }
}

// C# - 7.3

using NUnit.Framework;
using System;

[TestFixture]
public class IQTests {
    [Test]
    public void Test1() {
        Assert.AreEqual(3, IQ.Test("2 4 7 8 10"));
    }

    [Test]
    public void Test2() {
        Assert.AreEqual(1, IQ.Test("1 2 2"));
    }
}

// C# - 7.3

using System;
using NUnit.Framework;

[TestFixture]
public class FinanceTests {
    [Test]
    public void Test01() {
        Assert.AreEqual(105, Finance.finance(5));
    }

    [Test]
    public void Test02() {
        Assert.AreEqual(168, Finance.finance(6));
    }

    [Test]
    public void Test03() {
        Assert.AreEqual(360, Finance.finance(8));
    }

    [Test]
    public void Test04() {
        Assert.AreEqual(2040, Finance.finance(15));
    }
}

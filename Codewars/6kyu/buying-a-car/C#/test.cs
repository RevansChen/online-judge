// C# - 7.3

using System;
using NUnit.Framework;

[TestFixture]
public class BuyCarTests {
    [Test]
    public void Test1() {
        int[] r = new int[] { 6, 766 };
        Assert.AreEqual(r, BuyCar.nbMonths(2000, 8000, 1000, 1.5));
    }

    [Test]
    public void Test2() {
        int[] r = new int[] { 0, 4000 };
        Assert.AreEqual(r, BuyCar.nbMonths(12000, 8000, 1000, 1.5));
    }
}

// C# - 7.3

using NUnit.Framework;
using System;

[TestFixture]
public class LineTests {
    [Test]
    public void Test1() {
        int[] peopleInLine = new int[] {25, 25, 50, 50};
        Assert.AreEqual("YES", Line.Tickets(peopleInLine));
    }

    [Test]
    public void Test2() {
        int[] peopleInLine = new int[] {25, 100};
        Assert.AreEqual("NO", Line.Tickets(peopleInLine));
    }
}

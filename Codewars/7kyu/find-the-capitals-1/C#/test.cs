// C# - 7.3

using NUnit.Framework;

[TestFixture]
public class Tests {
    [Test]
    public void CodEWaRs() {
        Assert.AreEqual(Kata.Capitals("CodEWaRs"), new int[]{0, 3, 4, 6});
    }
}

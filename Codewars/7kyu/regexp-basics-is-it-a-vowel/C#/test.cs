// C# - 7.3

using System;
using System.Text;
using System.Text.RegularExpressions;
using NUnit.Framework;

[TestFixture]
public class KataTest {
    [Test]
    public void BasicTests() {
        Assert.AreEqual(false, "".Vowel());
        Assert.AreEqual(true, "a".Vowel());
        Assert.AreEqual(true, "E".Vowel());
        Assert.AreEqual(false, "ou".Vowel());
        Assert.AreEqual(false, "z".Vowel());
        Assert.AreEqual(false, "lol".Vowel());
    }
}

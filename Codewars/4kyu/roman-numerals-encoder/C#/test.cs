using System;
using NUnit.Framework;

[TestFixture]
public class RomanConvertTests {
  	[TestCase(1, "I"),
     TestCase(4, "IV"),
     TestCase(6, "VI"),
     TestCase(182, "CLXXXII"),
     TestCase(1990, "MCMXC"),
     TestCase(1875, "MDCCCLXXV"),
     TestCase(2008, "MMVIII"),
     TestCase(1666, "MDCLXVI"),
     TestCase(1000, "M"),
     TestCase(2007, "MMVII")]
	public void Test(int value, string expected) {
	  	Assert.AreEqual(expected, RomanConvert.Solution(value));
	}
}
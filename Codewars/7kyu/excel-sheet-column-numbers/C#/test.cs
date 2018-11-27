// C# - 7.3

using System;
using NUnit.Framework;

[TestFixture]
public class ExcelToNumberTests {

    [Test]
    public void Test1() {
        Console.WriteLine("****** Basic Tests");
        Assert.AreEqual(1, ExcelToNumber.TitleToNumber("A"));
        Assert.AreEqual(27, ExcelToNumber.TitleToNumber("AA"));
        Assert.AreEqual(52, ExcelToNumber.TitleToNumber("AZ"));
        Assert.AreEqual(53, ExcelToNumber.TitleToNumber("BA"));
        Assert.AreEqual(28779382963L, ExcelToNumber.TitleToNumber("CODEWARS"));
    }
}

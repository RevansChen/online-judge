// C# - 7.3

using System;
using System.Collections.Generic;
using System.Linq;

public class ExcelToNumber {
    public static long TitleToNumber(string title) =>
        title.Select((c, i) => (long)(((long)c - (long)'A' + 1) * (Math.Pow(26, title.Length - i - 1))))
             .Sum(v => v);
}

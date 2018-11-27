// C# - 7.3

using System;
using System.Linq;

public static class Kata {
    public static long DescendingOrder(long num) =>
        long.Parse(
            string.Concat(
                from c in num.ToString()
                orderby c descending
                select c
            )
        );
}

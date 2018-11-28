// C# - 7.3

using System;
using System.Linq;

public static class Kata {
    public static int[] Capitals(string word) =>
        word.Select((c, i) => (char.IsUpper(c) ? i : -1))
            .Where(i => (i >= 0))
            .ToArray();
}

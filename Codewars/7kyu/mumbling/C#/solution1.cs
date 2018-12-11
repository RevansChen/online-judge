// C# - 7.3

using System;
using System.Linq;

public class Accumul {
    public static String Accum(string s) =>
        string.Join("-",
            s.Select((c, i) =>
                char.ToUpper(c).ToString().PadRight(i + 1, char.ToLower(c))
            )
        );
}

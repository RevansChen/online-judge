// C# - 7.3

using System;

public class Kata {
    public static bool IsPronic(int n) {
        if (n < 0) {
            return false;
        }
        int i = (int)Math.Floor(Math.Sqrt(n));
        return (i * (i + 1)) == n;
    }
}

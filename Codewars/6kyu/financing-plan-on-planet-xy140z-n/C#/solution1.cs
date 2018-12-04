// C# - 7.3

public class Finance {
    public static ulong finance(ulong n) =>
        (n > 0) ? ((3 * n * (n + 1)) / 2 + finance(n - 1)) : 0;
}

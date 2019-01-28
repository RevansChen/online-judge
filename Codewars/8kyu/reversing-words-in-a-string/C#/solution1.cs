// C# - 7.3

using System.Linq;

public class Kata {
    public static string Reverse(string text) => string.Join(" ", text.Split(' ').Reverse());
}

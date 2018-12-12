// C# - 7.3

public static class Kata {
    public static bool Vowel(this string s) =>
        (s.Length == 1) && "aeiou".Contains(s.ToLower());
}

// C# - 7.3

using System;

public class Kata {
    public static bool All(int[] arr, Func<int, bool> fun) {
        foreach (int e in arr) {
            if (!fun(e)) {
                return false;
            }
        }
        return true;
    }
}

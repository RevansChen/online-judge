// C# - Mono 4.2.3

using System;

public static class Kata {
    public static Func<int, int> GetFunction(int[] sequence) {
        int m = sequence[0];
        int n = sequence[1] - sequence[0];
        if (!isLinear(sequence)) {
            throw new ArgumentException();
        }

        return new Func<int, int>(x => n * x + m);
    }

    private static bool isLinear(int[] sequence) {
        int d = sequence[1] - sequence[0];
        for (int i = 1; i < 4; ++i) {
            if ((sequence[i + 1] - sequence[i]) != d) {
                return false;
            }
        }

        return true;
    }
}


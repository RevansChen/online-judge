// C# - 7.3

using System;
using System.Collections.Generic;

public class NbInSum {
    public static long[][] Decompose(long n) {
        List<long> kns = new List<long>();
        long x = 2;
        while (n > 0) {
            long kn = (long)(Math.Log(n, x));
            if (kn <= 1) {
                break;
            }
            kns.Add(kn);
            n -= (long)Math.Pow(x, kn);
            x++;
        }

        return new long[][] { kns.ToArray() , new long[] { n } };
    }
}

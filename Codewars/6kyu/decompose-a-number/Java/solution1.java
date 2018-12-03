// Java - 1.8.0_91 (Java 8)

import java.util.ArrayList;
import java.lang.Math;

public class NbInSum {
    public static long[][] decompose(long n) {
        ArrayList<Long> kns = new ArrayList<Long>();
        long x = 2;
        while (n > 0) {
            long kn = (long)(Math.log(n) / Math.log(x));
            if (kn <= 1) {
                break;
            }
            kns.add(kn);
            n -= (long)Math.pow(x, kn);
            x++;
        }

        long[] a1 = new long[kns.size()];
        for (int i = 0; i < kns.size(); ++i) {
            a1[i] = kns.get(i);
        }

        return new long[][] { a1, { n } };
    }
}

// C# - 7.3

using System;
using System.Collections.Generic;

public class Line {
    public static string Tickets(int[] peopleInLine) {
        Dictionary<int, int> moneys = new Dictionary<int, int>() {
            [25] = 0, [50] = 0, [100] = 0
        };
        foreach (int p in peopleInLine) {
            switch (p) {
                case 50:
                    if (moneys[25] < 1) {
                        return "NO";
                    }
                    moneys[25]--;
                    break;

                case 100:
                    if (moneys[50] >= 1) {
                        if (moneys[25] < 1) {
                            return "NO";
                        }
                        moneys[50]--;
                        moneys[25]--;
                    }
                    else {
                        if (moneys[25] < 3) {
                            return "NO";
                        }
                        moneys[25] -= 3;
                    }
                    break;
            }
            moneys[p]++;
        }
        return "YES";
    }
}

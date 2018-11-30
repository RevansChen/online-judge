// C# - 7.3

using System;
using System.Collections.Generic;

public class BuyCar {
    public static int[] nbMonths(int startPriceOld, int startPriceNew, int savingperMonth, double percentLossByMonth) {
        double priceOld = startPriceOld;
        double priceNew = startPriceNew;
        int month = 0;
        double money = priceOld - priceNew;
        double loss = percentLossByMonth / 100.0;

        while (money < 0) {
            if ((++month % 2) == 0) {
                loss += 0.005;
            }
            priceOld *= 1 - loss;
            priceNew *= 1 - loss;
            money = priceOld - priceNew + savingperMonth * month;
        }

        return new int[] { month, (int)Math.Round(money) };
    }
}

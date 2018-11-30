// C++ - 14

#include <cmath>

class BuyCar {
public:
    static std::vector<int> nbMonths(int startPriceOld, int startPriceNew, int savingperMonth, double percentLossByMonth) {
        std::vector<int> results;

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

        results.push_back(month);
        results.push_back((int)round(money));
        return results;
    }
};

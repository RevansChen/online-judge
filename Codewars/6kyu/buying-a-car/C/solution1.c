// C - Clang 3.6 / C11

int* nbMonths(int startPriceOld, int startPriceNew, int savingperMonth, double percentLossByMonth) {
    int* results = (int*)malloc(sizeof(int) * 2);

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

    results[0] = month;
    results[1] = (int)round(money);
    return results;
}

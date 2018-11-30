# Python - 3.6.0

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    priceOld, priceNew = startPriceOld, startPriceNew
    loss = percentLossByMonth / 100.0
    month, cash = 0, 0
    while (priceOld + cash) < priceNew:
        month += 1
        if (month % 2) == 0:
            loss += 0.005
        priceOld *= (1 - loss)
        priceNew *= (1 - loss)
        cash += savingperMonth
    return [month, round((priceOld + cash) - priceNew)]

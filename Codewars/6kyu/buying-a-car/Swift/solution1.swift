// Swift - 4

func nbMonths(_ startPriceOld: Int, _ startPriceNew: Int, _ savingPerMonth: Int, _ percentLossByMonth: Double) -> (Int, Int) {
    var priceOld: Double = Double(startPriceOld)
    var priceNew: Double = Double(startPriceNew)
    var month: Int = 0
    var money: Double = priceOld - priceNew
    var loss: Double = percentLossByMonth / 100.0

    while money < 0 {
        month += 1
        if month % 2 == 0 {
            loss += 0.005
        }
        priceOld *= (1 - loss)
        priceNew *= (1 - loss)
        money = priceOld - priceNew + Double(savingPerMonth * month)
    }

    return (month, Int(round(money)))
}

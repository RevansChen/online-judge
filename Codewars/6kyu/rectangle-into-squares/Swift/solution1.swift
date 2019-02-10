// Swift - 4

func sqInRect(_ lng: Int, _ wdth: Int) -> [Int]? {
    if lng == wdth {
        return nil
    }
    var w = wdth
    var l = lng
    if l > w {
        (w, l) = (l, w)
    }
    var results = [Int]()
    while (w > 0) && (l > 0) {
        results.append(l)
        let nl = w - l
        (w, l) = (max(l, nl), min(l, nl))
    }
    return results
}

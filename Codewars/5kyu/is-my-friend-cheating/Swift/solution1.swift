// Swift - 4

func removNb(_ n: Int) -> [(Int, Int)] {
    var results = [(Int, Int)]()
    let sum: Int = (1 + n) * n / 2
    for a in 1...n {
        let (x, y) = (sum - a, 1 + a)
        let (b, rem) = (x / y, x % y)
        if (rem == 0) && (1 <= b) && (b < n) {
            results.append((a, b))
        }
    }
    return results
}

// Swift - 4

func expandedForm(_ num: Int) -> String {
    var num: Int = num
    var values: [String] = []
    var zero: String = ""

    while num > 0 {
        let n = num % 10
        if n > 0 {
            values.append("\(n)\(zero)")
        }
        num /= 10
        zero += "0"
    }
    return values.reversed().joined(separator: " + ")
}

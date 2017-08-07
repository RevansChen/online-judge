string solution(int n) {
    // 列出所有可能的進位值
    map<int, string> symbols = {
        {1000, "M"}, 
        {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, 
        {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, 
        {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
    };
    
    string result = "";
    map<int, string>::reverse_iterator rit = symbols.rbegin();
    for (; (rit != symbols.rend()) && (n > 0); ++rit) {
        // 符號出現次數
        for (int i = 0; i < (n / rit->first); ++i) {
            result += rit->second;
        }
        // 剩餘位數
        n %= rit->first;
    }
        
    return result;
}
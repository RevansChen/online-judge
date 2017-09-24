// JavaScript - Node v6.11.0

function solution(n) {
    // 列出所有可能的進位值
    var symbols = {
        M: 1000, 
        CM: 900, D: 500, CD: 400, C: 100, 
        XC: 90, L: 50, XL: 40, X: 10, 
        IX: 9, V: 5, IV: 4, I: 1
    }
    
    var result = "";
    for (var r in symbols) {
        if (n <= 0) {
            break;
        }
        // 符號出現次數
        for (var i = 0; i < parseInt(n / symbols[r]); ++i) {
            result += r;
        }
        // 剩餘位數
        n %= symbols[r];
    }
        
    return result;
}
function solution(n) {
    // 範圍限制，範圍外不處理
    // JavaScript有超過4000的測資，故去除限制在4000內的判斷
    if (n <= 0) {
        return "";
    }
    
    var symbols = "IVXLCDM";
    var result = "";
    
    // 轉換方式為
    // 將symbol兩個作為一組，並加上下一組的較小的那一個
    // step   group
    //   1    IV + X
    //   2    XL + C
    //   3    CD + M
    var i = 0;
    while (n) {
        var v = n % 10;             // 目前位數
        n = parseInt(n / 10);       // 剩餘位數
        var p5 = parseInt(v / 5);   // 計算出5的數量
        var p1 = v % 5;             // 計算出1的數量
        
        var r = "";
        if (symbols[i] == "M") {
            // 針對大於4000的數值做處理，因為沒有對應的符號所以全用M取代
            // 實際上應該要是
            //                   _         _
            // 1000 = M, 4000 = MV, 5000 = V
            var t = n * 10 + v;
            for (var j = 0; j < t; ++j) {
                r += symbols[i];
            }
        }
        else {
            if (p1 == 4) {
                // 針對1數量為4個做處理，從加法變減法
                // 小的在前 (I)，大的在後 (V 或 X)
                r = symbols[i] + symbols[i + 1 + p5];
            }
            else {
                // 1數量為0~3個的為加法
                if (p5) {
                    r = symbols[i + 1];     // V
                }
                for (var j = 0; j < p1; ++j) {
                    r += symbols[i];        // I, II, III
                }
            }
        }
        
        result = r + result;
        i += 2;
    }
        
    return result;
}
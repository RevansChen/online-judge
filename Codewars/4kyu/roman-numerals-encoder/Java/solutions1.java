public class Conversion {
    public String solution(int n) {
        // 範圍限制，大於等於4000以上的無對應符號，所以不處理
        if ((n <= 0) || (n >= 4000)) {
            return "";
        }
        
        String symbols = "IVXLCDM";
        String result = "";
        
        // 轉換方式為
        // 將symbol兩個作為一組，並加上下一組的較小的那一個
        // step   group
        //   1    IV + X
        //   2    XL + C
        //   3    CD + M
        int i = 0;
        while (n > 0) {
            int v = n % 10;     // 目前位數
            n = n / 10;         // 剩餘位數
            int p5 = v / 5;     // 計算出5的數量
            int p1 = v % 5;     // 計算出1的數量
            
            String r = "";
            if (p1 == 4) {
                // 針對1數量為4個做處理，從加法變減法
                // 小的在前 (I)，大的在後 (V 或 X)
                int j = i + 1 + p5;
                r = symbols.substring(i, i + 1) + symbols.substring(j, j + 1);
            }
            else {
                // 1數量為0~3個的為加法
                if (p5 > 0) {
                    int j = i + 1;
                    r = symbols.substring(j, j + 1);    // V
                }
                for (int j = 0; j < p1; ++j) {
                    r += symbols.substring(i, i + 1);   // I, II, III
                }
            }
            
            result = r + result;
            i += 2;
        }
            
        return result;
    }
}
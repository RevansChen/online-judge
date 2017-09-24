// Java - 1.8.0_91(Java 8)

import java.util.Map;
import java.util.LinkedHashMap;

public class Conversion {
    public String solution(int n) {
        Map<Integer, String> symbols = new LinkedHashMap<Integer, String>();
        symbols.put(1000, "M"); 
        symbols.put(900, "CM"); symbols.put(500, "D"); symbols.put(400, "CD"); symbols.put(100, "C"); 
        symbols.put(90, "XC"); symbols.put(50, "L"); symbols.put(40, "XL"); symbols.put(10, "X"); 
        symbols.put(9, "IX"); symbols.put(5, "V"); symbols.put(4, "IV"); symbols.put(1, "I");
        
        String result = "";
        for (Map.Entry<Integer, String> symbol: symbols.entrySet()) {
            if (n <= 0) {
                break;
            }
            // 符號出現次數
            for (int i = 0; i < (n / symbol.getKey()); ++i) {
                result += symbol.getValue();
            }
            // 剩餘位數
            n %= symbol.getKey();
        }
            
        return result;
    }
}
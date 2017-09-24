// Mono - 4.2.3

using System;
using System.Collections.Generic;
using NumSymb = System.Tuple<int, string>;

public class RomanConvert {
    public static string Solution(int n) {
        // 列出所有可能的進位值
        List<NumSymb> symbols = new List<NumSymb>() { 
            new NumSymb(1000, "M"), 
            new NumSymb(900, "CM"), new NumSymb(500, "D"), new NumSymb(400, "CD"), new NumSymb(100, "C"), 
            new NumSymb(90, "XC"), new NumSymb(50, "L"), new NumSymb(40, "XL"), new NumSymb(10, "X"), 
            new NumSymb(9, "IX"), new NumSymb(5, "V"), new NumSymb(4, "IV"), new NumSymb(1, "I")
        };
        
        string result = "";
        foreach (NumSymb symbol in symbols) {
            if (n <= 0) {
                break;
            }
            
            // 符號出現次數
            for (int i = 0; i < (n / symbol.Item1); ++i) {
                result += symbol.Item2;
            }
            // 剩餘位數
            n %= symbol.Item2;
        }
            
        return result;
    }
}

// JavaScript - Node v6.11.0

function squareArea(A) {
    // 將數值四捨五入到指定的位數
    function round10(val, dec) {
        var scale = Math.pow(10, dec);
        return Math.round(val * scale) / scale;
    }
    
    // 利用弧長計算出半徑
    var r = 2 * A / Math.PI;
    
    // 計算出正方形面積, 並四捨五入到小數第二位
    return round10(r * r, 2);
}
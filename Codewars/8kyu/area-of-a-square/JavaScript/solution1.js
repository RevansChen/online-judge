// JavaScript - Node v8.1.3

function squareArea(A) {
    function round10(val, dec) {
        var scale = Math.pow(10, dec);
        return Math.round(val * scale) / scale;
    }
    var r = 2 * A / Math.PI;
    return round10(r * r, 2);
}

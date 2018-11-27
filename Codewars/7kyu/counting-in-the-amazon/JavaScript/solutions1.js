// JavaScript - Node v8.1.3

function countArara(n) {
    var r = [];
    for (var i = 0; i < (n >> 1); ++i) {
        r.push("adak");
    }
    if (n % 2) {
        r.push("anane");
    }
    return r.join(" ");
}

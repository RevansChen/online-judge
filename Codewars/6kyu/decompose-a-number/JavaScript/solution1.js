// JavaScript - Node v8.1.3

function decompose(num) {
    let kns = [];
    let kn;
    for (let x = 2; x * x <= num; num -= Math.pow(x++, kn)) {
        kn = Math.floor(Math.log(num) / Math.log(x));
        kns.push(kn);
    }
    return [kns, num];
}

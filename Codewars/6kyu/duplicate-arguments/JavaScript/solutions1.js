// JavaScript - Node v8.1.3

function solution(...args) {
    var map = {};
    for (var i in args) {
        if (args[i] in map) {
            return true;
        }
        map[args[i]] = true;
    }
    return false;
}

// JavaScript - Node v8.1.3

function createArgumentMap(func, ...args) {
    var output = [];
    var reg = /^function +\w*\((.*)\)/g;
    var str = func.toString().split(reg)[1].replace(' ', '');
    if (str) {
        var names = str.split(',');
        for (var i in names) {
            output[names[i]] = args[i];
        }
    }
    return output;
}

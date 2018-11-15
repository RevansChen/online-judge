// JavaScript - Node v8.1.3

function buildPyramid(str, n) {
    patterns = [];
    tmp = str[0];
    for (var i = 1; i < str.length; ++i) {
        if (str[i - 1] != str[i]) {
            patterns.push(tmp);
            tmp = '';
        }
        tmp += str[i];
    }
    patterns.push(tmp);
    
    output = [];
    for (var i = 1; i <= n; ++i) {
        tmp = '';
        for (var j in patterns) {
            tmp += patterns[j].repeat(i);
        }
        output.push(' '.repeat((str.length / 2) * (n - i)) + tmp);
    }
    return output.join('\n');
}

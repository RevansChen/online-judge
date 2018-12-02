// JavaScript - Node v8.1.3

function sign(x) {
    return x ? ((x < 0) ? -1 : 1) : 0;
}

function getFunction(sequence) {
    var n = sequence[1] - sequence[0];
    for (var i = 1; i < 4; ++i) {
        if ((sequence[i + 1] - sequence[i]) != n) {
            return 'Non-linear sequence';
        }
    }

    var ans = '';
    if (n == 1) {
        ans = 'x';
    }
    else if (n == -1) {
        ans = '-x';
    }
    else if (n != 0) {
        ans = n + 'x';
    }

    var m = sequence[0];
    if (ans == '') {
        ans = m.toString();
    }
    else {
        var s = sign(m);
        var v = Math.abs(m);

        if (s > 0) {
            ans += ' + ' + v;
        }
        else if (s < 0) {
            ans += ' - ' + v;
        }
    }

    return 'f(x) = ' + ans;
}

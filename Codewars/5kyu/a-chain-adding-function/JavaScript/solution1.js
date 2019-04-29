// JavaScript - Node v8.1.3

add = n => {
    let _add = x => add(n + x);
    _add.valueOf = _ => n;
    return _add;
};

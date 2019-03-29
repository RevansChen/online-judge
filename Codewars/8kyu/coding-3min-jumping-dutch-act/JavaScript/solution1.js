// JavaScript - Node v8.1.3

function sc(floor) {
    if (floor <= 1) {
        return '';
    }
    let voice = Array(floor - 1).fill('Aa~');
    voice.push('Pa!');
    if (floor <= 6) {
        voice.push('Aa!');
    }
    return voice.join(' ');
}

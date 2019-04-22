// JavaScript - Node v8.1.3

const changeMe = (moneyIn) => {
    let kv = {
        '£5':  Array(25).fill('20p'),
        '£2':  Array(10).fill('20p'),
        '£1':  Array(5).fill('20p'),
        '50p': Array(2).fill('20p').concat('10p'),
        '20p': Array(2).fill('10p')
    };
    return (kv[moneyIn] ? kv[moneyIn].join(' ') : moneyIn);
}

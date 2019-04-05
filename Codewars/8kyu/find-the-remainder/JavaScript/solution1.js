// JavaScript - Node v8.1.3

const remainder = (...a) => Math.min(...a) ? Math.max(...a) % Math.min(...a) : NaN;

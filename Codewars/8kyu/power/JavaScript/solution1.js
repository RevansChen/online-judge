// JavaScript - Node v8.1.3

const numberToPower = (number, power) => Array(power).fill(number).reduce((a, b) => a * b, 1);

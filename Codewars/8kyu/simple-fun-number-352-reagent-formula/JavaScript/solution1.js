// JavaScript - Node v8.1.3

function isValid(formula) {
    if ((formula.indexOf(1) != -1) && (formula.indexOf(2) != -1)) {
        return false;
    }
    if ((formula.indexOf(3) != -1) && (formula.indexOf(4) != -1)) {
        return false;
    }
    if ((formula.indexOf(5) != -1) ^ (formula.indexOf(6) != -1)) {
        return false;
    }
    if ((formula.indexOf(7) == -1) && (formula.indexOf(8) == -1)) {
        return false;
    }

    return true;
}

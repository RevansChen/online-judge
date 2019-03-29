# CoffeeScript - 1.10.0

weapons =
    PT92:  17
    M4A1:  30
    M16A2: 30
    PSG1:  5

magNumber = (info) -> (info[1] * 3) // weapons[info[0]] + 1

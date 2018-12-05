# Python - 3.6.0

NATO_TABLE = {
    'A': 'Alfa',    'B': 'Bravo',  'C': 'Charlie', 'D': 'Delta',    'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf',   'H': 'Hotel',   'I': 'India',    'J': 'Juliett',
    'K': 'Kilo',    'L': 'Lima',   'M': 'Mike',    'N': 'November', 'O': 'Oscar',
    'P': 'Papa',    'Q': 'Quebec', 'R': 'Romeo',   'S': 'Sierra',   'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',     'Y': 'Yankee',
    'Z': 'Zulu'
}

def to_nato(words):
    return ' '.join([
        NATO_TABLE.get(letter, letter) for letter in words.upper() if letter != ' '
    ])

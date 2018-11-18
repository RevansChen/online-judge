# Python - 3.4.3

def puzzle_tiles(width, height):
    puzzle = [ '  ' + ' _( )__' * width ]
    for i in range(height):
        if i % 2:
            puzzle.append(' |_' + '     |_' * width)
            puzzle.append('  _)' + ' _   _)' * width)
        else:
            puzzle.append(' _|' + '     _|' * width)
            puzzle.append('(_' + '   _ (_' * width)
        puzzle.append(' |' + '__( )_|' * width)
    return '\n'.join(puzzle)

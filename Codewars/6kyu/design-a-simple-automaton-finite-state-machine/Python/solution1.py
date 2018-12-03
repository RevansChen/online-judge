# Python - 3.6.0

class Automaton(object):
    LOGIC = {
        1: {'0': 1, '1': 2},
        2: {'0': 3, '1': 2},
        3: {'0': 2, '1': 2}
    }
    def read_commands(self, commands):
        state = 1
        for command in commands:
            state = Automaton.LOGIC[state][command]
        return (state == 2)

my_automaton = Automaton()

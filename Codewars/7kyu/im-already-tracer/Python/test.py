# Python - 3.6.0

@test.describe('Basic Tests')
def basic_tests():
    team = ['D.Va', 'Orisa', 'Ashe', 'Bastion', 'Ana', 'Mercy']
    test.assert_equals(team_comp(team), [2, 2, 2])
    team = ['Widowmaker', 'Tracer', 'Ashe', 'Bastion', 'Genji', 'Mercy']
    test.assert_equals(team_comp(team), [0, 5, 1])
    team = ['Reinhardt', 'Torbjörn', 'Mei', 'Pharah', 'Ana', 'Brigitte']
    test.assert_equals(team_comp(team), [1, 3, 2])

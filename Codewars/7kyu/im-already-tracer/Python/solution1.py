# Python - 3.6.0

def team_comp(heroes):
    if (len(heroes) != 6) or (len(heroes) != len(set(heroes))):
        raise InvalidTeam()
    team = [0, 0, 0]
    index = 0
    for hero in heroes:
        if hero in TANK:
            index = 0
        elif hero in DAMAGE:
            index = 1
        elif hero in SUPPORT:
            index = 2
        team[index] += 1
    return team

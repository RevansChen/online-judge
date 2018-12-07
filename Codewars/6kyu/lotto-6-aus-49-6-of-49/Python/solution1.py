# Python - 3.6.0

from random import randint

def number_generator():
    numbers = []
    while len(numbers) < 6:
        num = randint(1, 49)
        if not (num in numbers):
            numbers.append(num)
    numbers.sort()
    numbers.append(randint(0, 9))
    return numbers

categorys = {
    (6, 1): 1,
    (6, 0): 2,
    (5, 1): 3,
    (5, 0): 4,
    (4, 1): 5,
    (4, 0): 6,
    (3, 1): 7,
    (3, 0): 8,
    (2, 1): 9
}
def check_for_winning_category(your_numbers, winning_numbers):
    *yourNumbers, yourSuperzahl = your_numbers
    *winningNumbers, winningSuperzahl = winning_numbers

    matchCount = sum([int(num in winningNumbers) for num in yourNumbers])
    superzahlMatch = int(yourSuperzahl == winningSuperzahl)

    return categorys.get((matchCount, superzahlMatch), -1)

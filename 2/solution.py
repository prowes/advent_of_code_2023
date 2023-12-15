from functools import reduce

file = open('input.txt', 'r')
document = file.read().splitlines()

cubes_we_have = {"red": 12, "green": 13, "blue": 14}
possible_games_nums = set()

powers = 0
for game in document:
    cleared_lines = game.split(':')[1].split(';')
    minumum_cubes = {"red": 0, "green": 0, "blue": 0}
    impossible = False
    for game_set in cleared_lines:
        game_set_cleared = game_set.split(',')
        for cube in game_set_cleared:
            one_cube = cube.split(' ')
            color = one_cube[2]
            needed_amount = int(one_cube[1])
            if (needed_amount > cubes_we_have[color]):  # part one
               impossible = True
            if minumum_cubes[color] < needed_amount:  # part two
                minumum_cubes[color] = needed_amount
    if impossible == False:
        possible_games_nums.add(document.index(game) + 1)
    one_power = reduce((lambda x, y: x * y), list(minumum_cubes.values()))
    powers += one_power
print(sum(possible_games_nums))
print(powers)

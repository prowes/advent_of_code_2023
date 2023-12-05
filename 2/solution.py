file = open('input.txt', 'r')
document = file.read().splitlines()

cubes_we_have = {"red": 12, "green": 13, "blue": 14}
possible_games_nums = set()

for game in document:
    cleared_lines = game.split(':')[1].split(';')
    impossible = False
    for game_set in cleared_lines:
        game_set_cleared = game_set.split(',')
        for cube in game_set_cleared:
            one_cube = cube.split(' ')
            color = one_cube[2]
            needed_amount = int(one_cube[1])
            if (needed_amount > cubes_we_have[color]):
               print(f"NOT ENOUGH {one_cube[2]} CUBE, {needed_amount} needed, we have {cubes_we_have[color]}")
               print(f"game {document.index(game) + 1} not enough")
               impossible = True
    if impossible == False:
        print("Possible games are:")
        print(document.index(game) + 1)
        possible_games_nums.add(document.index(game) + 1)
print(sum(possible_games_nums))
#! /usr/bin/env python3

from functools import reduce

def get_power(game):
    min_col = {'red': 0, 'green': 0, 'blue': 0}
    for draw in game.split(';'):
        for pair in draw.split(','):
            num, color, *_ = pair.split()
            if int(num) > min_col[color]:
                min_col[color] = int(num)
    return reduce(lambda a, b: a * b, min_col.values())


res = 0
with open('input.txt') as f:
    for index, line in enumerate(f.readlines()):
        game = line.split(':')[1].strip()
        res += get_power(game)
    print(res)

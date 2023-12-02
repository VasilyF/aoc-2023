#! /usr/bin/env python3

max_color = {'red': 12, 'green': 13, 'blue': 14}

def is_possible(game):
    for draw in game.split(';'):
        for pair in draw.split(','):
            num, color, *_ = pair.split()
            if int(num) > max_color[color]:
                return False
    return True


res = 0
with open('input.txt') as f:
    for index, line in enumerate(f.readlines()):
        game = line.split(':')[1].strip()
        if is_possible(game):
            res += index + 1
    print(res)



#! /usr/bin/env python3

pipes = {'|': {'n': 'n', 's': 's'}, # {curr_dir: next_dir}
         '-': {'w': 'w', 'e': 'e'}, 
         'L': {'s': 'e', 'w': 'n'}, 
         'J': {'s': 'w', 'e': 'n'}, 
         '7': {'n': 'w', 'e': 's'}, 
         'F': {'n': 'e', 'w': 's'}}

dir_deltas = {'n': (-1, 0), 'e': (0, 1), 's': (1, 0), 'w': (0, -1)}

with open('input.txt') as f:
    lines = f.readlines()

grid = []
loc = None
grid.append(['.']*(len(lines[0].strip())+2))
for i, line in enumerate(lines):
    i = i + 1
    grid.append(list('.' + line.strip() + '.'))
    if loc is None and 'S' in grid[i]:
        loc = (i, grid[i].index('S'))
grid.append(['.']*(len(lines[0].strip())+2))


def next_state(state):
    loc, direct = state
    i  = loc[0] + dir_deltas[direct][0]
    j  = loc[1] + dir_deltas[direct][1]
    next_loc = (i, j)
    next_sym = grid[i][j]
    next_direct = pipes[next_sym][direct]
    return next_loc, next_direct


# check all the possible connecting pipe locations
# at starting location
states = []
for direct in 'nesw':
    i  = loc[0] + dir_deltas[direct][0]
    j  = loc[1] + dir_deltas[direct][1]
    sym = grid[i][j]
    if sym in pipes and direct in pipes[sym]:
        states.append((loc, direct))

steps = 0
while states[0][0] != states[1][0] or steps == 0:
    # take step
    steps += 1
    states = list(map(next_state, states))

print(steps)

#! /usr/bin/env python3

pipes = {'|': {'n': 'n', 's': 's'}, # {curr_dir: next_dir}
         '-': {'w': 'w', 'e': 'e'}, 
         'L': {'s': 'e', 'w': 'n'}, 
         'J': {'s': 'w', 'e': 'n'}, 
         '7': {'n': 'w', 'e': 's'}, 
         'F': {'n': 'e', 'w': 's'}, 
         'S': None}

dir_deltas = {'n': (-1, 0), 'e': (0, 1), 's': (1, 0), 'w': (0, -1)}

with open('input.txt') as f:
    lines = f.readlines()

grid = []
init_loc = None
grid.append(['.']*(len(lines[0].strip())+2))
for i, line in enumerate(lines):
    i = i + 1
    grid.append(list('.' + line.strip() + '.'))
    if init_loc is None and 'S' in grid[i]:
        init_loc = (i, grid[i].index('S'))
grid.append(['.']*(len(lines[0].strip())+2))

# check all the possible connecting pipe locations
# at starting location
init_direct = None
for direct in 'nesw':
    i  = init_loc[0] + dir_deltas[direct][0]
    j  = init_loc[1] + dir_deltas[direct][1]
    sym = grid[i][j]
    if sym in pipes and direct in pipes[sym]:
        init_direct = direct
        break

classification = []
for i in range(len(grid)):
    row = []
    for j in range(len(grid[0])):
        row.append('.')
    classification.append(row)


def step(state):
    loc, direct = state
    i  = loc[0] + dir_deltas[direct][0]
    j  = loc[1] + dir_deltas[direct][1]
    next_loc = (i, j)
    next_sym = grid[i][j]

    # hack
    if next_sym == 'S': 
        return next_loc, init_direct

    # print('next:', next_loc, next_sym)
    next_direct = pipes[next_sym][direct]
    return next_loc, next_direct


def update_class(loc, direct):
    global classification
    # A represents left hand rule curl (relative to direct)
    # B represents right hand rule curl (relative to direct)
    # P represents previously encountered pipe element
    # . represents undetermined
    i_curr, j_curr = loc
    classification[i_curr][j_curr] = grid[i_curr][j_curr]

    # classify perpendicular cells
    # ... P R R R ^ L L L P ...
    match direct:
        case 'n' | 's':
            for j in range(j_curr - 1, -1, -1):
                if classification[i_curr][j] in pipes:
                    break
                classification[i_curr][j] = 'B' if direct == 'n' else 'A'

            for j in range(j_curr + 1, len(classification[i_curr])):
                if classification[i_curr][j] in pipes:
                    break
                classification[i_curr][j] = 'A' if direct == 'n' else 'B'

        case 'e' | 'w':
            for i in range(i_curr - 1, -1, -1):
                if classification[i][j_curr] in pipes:
                    break
                classification[i][j_curr] = 'B' if direct == 'e' else 'A'

            for i in range(i_curr + 1, len(classification)):
                if classification[i][j_curr] in pipes:
                    break
                classification[i][j_curr] = 'A' if direct == 'e' else 'B'


state = (init_loc, init_direct)
update_class(state[0], state[1])
steps = 0
while state[0] != init_loc or steps == 0:
    # take step
    steps += 1
    next_state = step(state)
    if next_state[1] != state[1]:
        update_class(next_state[0], state[1])
    update_class(next_state[0], next_state[1])
    state = next_state

# determine 'outside' character
# padding will necessary be outside inner loop
# check a determined cell part of padding
i, j = init_loc
if init_direct == 'n' or init_direct == 's':
    outside = classification[i][0]
else:
    outside = classification[0][j]

inside = 'A' if outside == 'B' else 'B'
res = 0
for row in classification:
    for cell in row:
        if cell == inside:
            res += 1

print(res)

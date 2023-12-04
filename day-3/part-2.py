#!/usr/bin/env python3

mat = []
bounds = []
res = 0

def add_bound(digit, row, start, end):
    left_col = max(0, start - 1)
    right_col = min(len(mat[0]) - 1, end + 1)

    # top row
    if row != 0:
        for i in range(left_col, right_col + 1):
            bounds[row - 1][i].append(digit)
    
    # bottom row
    if row != len(mat) - 1:
        for i in range(left_col, right_col + 1):
            bounds[row + 1][i].append(digit)

    # edges
    if start != 0:
        bounds[row][start - 1].append(digit)
    if end != len(mat[0]) - 1:
        bounds[row][end + 1].append(digit)


with open('input.txt') as f:
    mat = f.readlines()
    # remove return characters
    for i in range(len(mat)):
        mat[i] = mat[i].strip()

    for i in range(len(mat)):
        bounds.append([])
        for j in range(len(mat[0])):
            bounds[i].append([])

    gears = []

    for i, line in enumerate(mat):
        digit_start = digit_end = None
        for j, c  in enumerate(line):

            # keep track of location of gears
            if c == '*':
                gears.append((i, j))

            # set start digit index
            if digit_start is None and c.isdigit():
                digit_start = j

            # set end digit index 
            if digit_start is None: continue

            if j + 1 == len(line) or not mat[i][j + 1].isdigit():
                digit_end = j

                # add digit to boundary
                digit = int(mat[i][digit_start:digit_end + 1]) 
                add_bound(digit, i, digit_start, digit_end)
                digit_start = digit_end = None

    # boundaries that overlap with gears
    for i, j in gears:
        overlapping = bounds[i][j]
        if len(overlapping) == 2:
            res += overlapping[0] * overlapping[1] 

print(res)

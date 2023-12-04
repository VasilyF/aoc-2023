#!/usr/bin/env python3

mat = []
res = 0

def is_part(row, start, end):
    left_col = max(0, start - 1)
    right_col = min(len(mat[0]) - 1, end + 1)

    # top row
    if row != 0:
        for i in range(left_col, right_col + 1):
            if mat[row - 1][i] != '.': return True
    
    # bottom row
    if row != len(mat) - 1:
        for i in range(left_col, right_col + 1):
            if mat[row + 1][i] != '.': return True

    # edges
    if start != 0 and mat[row][left_col] != '.':
        return True
    if end != len(mat[0]) - 1 and mat[row][right_col] != '.':
        return True

    return False


with open('input.txt') as f:
    mat = f.readlines()
    # remove return characters
    for i in range(len(mat)):
        mat[i] = mat[i].strip()

    for i, line in enumerate(mat):
        digit_start = digit_end = None
        for j, c  in enumerate(line):
            # set start digit index
            if digit_start is None and c.isdigit():
                digit_start = j

            # set end digit index 
            if digit_start is None: continue

            if j + 1 == len(line) or not mat[i][j + 1].isdigit():
                digit_end = j

                # check surrounding
                if is_part(i, digit_start, digit_end):
                    digit = int(mat[i][digit_start:digit_end + 1]) 
                    res += digit 

                digit_start = digit_end = None

print(res)

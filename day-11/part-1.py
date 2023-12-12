#! /usr/bin/env python3

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

galaxies = []
# new distance at original location
dists_i = []
dists_j = []

# determine space expansions in y
for i, row in enumerate(lines):
    d = -1 if i == 0 else dists_i[-1] 
    d += 2 if '#' not in row else 1
    dists_i.append(d)

# finds galaxies and expansions in x
for j in range(len(lines[0])):
    has_galaxies = False

    for i in range(len(lines)):
        cell = lines[i][j]
        if cell == '#':
            galaxies.append((i, j))
            has_galaxies = True

    d = -1 if j == 0 else dists_j[-1] 
    d += 2 if not has_galaxies else 1
    dists_j.append(d)

res = 0
for i, first in enumerate(galaxies[:-1]):
    for second in galaxies[i+1:]:
        dist_i = abs(dists_i[first[0]] - dists_i[second[0]])
        dist_j = abs(dists_j[first[1]] - dists_j[second[1]])
        res += dist_i + dist_j

print(res)

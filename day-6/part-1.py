#! /usr/bin/env python3

with open('input.txt') as f:
    lines = f.readlines()

times = list(map(int, lines[0].split(':')[1].split()))
dists = list(map(int, lines[1].split(':')[1].split()))

res = 1
for i, time in enumerate(times):
    res *= len(list(filter(lambda x: x > dists[i], [t*(time-t) for t in range(1, time)])))

print(res)

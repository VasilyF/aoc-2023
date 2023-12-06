#! /usr/bin/env python3

with open('input.txt') as f:
    lines = f.readlines()

time = int(''.join(lines[0].split(':')[1].split()))
dist = int(''.join(lines[1].split(':')[1].split()))

print(len(list(filter(lambda x: x > dist, [t*(time-t) for t in range(1, time)]))))

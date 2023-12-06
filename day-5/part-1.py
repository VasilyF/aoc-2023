#! /usr/bin/env python3

# https://grantjenks.com/docs/sortedcontainers
from sortedcontainers import SortedList

with open('input.txt') as f:
    lines = f.readlines()

seeds = [int(i) for i in lines[0].split(':')[1].split()]

inputs = SortedList(seeds)

def apply_mapping(entries):
    global inputs
    outputs = list(inputs)

    for entry in entries:
        out_start, in_start, length = tuple([int(i) for i in entry.split()])
        left = inputs.bisect_left(in_start)
        right = inputs.bisect_left(in_start + length)

        for i in range(left, right):
            diff = inputs[i] - in_start
            outputs[i] = out_start + diff

    inputs = SortedList(outputs)

# there are 7 mapping blocks, each separated by blank line
block_start = 3
lines.append('\n')
for _ in range(7):
    block_end = lines[block_start::].index('\n') + block_start
    block = lines[block_start:block_end]
    apply_mapping(block)
    block_start = block_end + 2

print(min(inputs))

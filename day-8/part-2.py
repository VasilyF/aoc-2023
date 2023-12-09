#! /usr/bin/env python3
from math import lcm

with open('input.txt') as f:
    lines = f.readlines()

instructions = lines[0].strip()
period = len(instructions)

nodes = {}
for line in lines[2::]:
    node, rl = line.strip().split(' = ')
    r, l = rl[1:-1].split(', ')
    nodes[node] = (r, l)

def get_cycle(symbol):
    curr_symbol = symbol
    curr_node = nodes[curr_symbol]
    ins_i = 0
    period_z = None # z may be in subloop
    steps_to_z = None # assume will always include a z link
    while True:
        ins = instructions[ins_i % period]

        # take step
        curr_symbol = curr_node[0] if ins == 'L' else curr_node[1]
        curr_node = nodes[curr_symbol]
        ins_i += 1

        if curr_symbol[-1] == 'Z':
            if steps_to_z is None:
                steps_to_z = ins_i
            else:
                period_z = ins_i - steps_to_z
                return steps_to_z, period_z


starts = list(filter(lambda x: x[-1] == 'A', nodes.keys()))
cycles = list(map(get_cycle, starts))

print(lcm(*[x[1] for x in cycles]))

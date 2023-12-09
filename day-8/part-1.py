#! /usr/bin/env python3

with open('input.txt') as f:
    lines = f.readlines()

instructions = lines[0].strip()
nodes = {}
for line in lines[2::]:
    node, rl = line.strip().split(' = ')
    r, l = rl[1:-1].split(', ')
    nodes[node] = (r, l)

curr_symbol = 'AAA'
curr_node = nodes[curr_symbol]
ins_i = 0
period = len(instructions)
while curr_symbol != 'ZZZ':
    ins = instructions[ins_i % period]
    curr_symbol = curr_node[0] if ins == 'L' else curr_node[1]
    curr_node = nodes[curr_symbol]
    ins_i += 1

print(ins_i)


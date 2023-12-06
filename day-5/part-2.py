#! /usr/bin/env python3

with open('input.txt') as f:
    lines = f.readlines()

values = [int(i) for i in lines[0].split(':')[1].split()]
# inputs are range (inc, exc)
inputs = set([(values[i], values[i] + values[i+1]) for i in range(0, len(values), 2)])

def apply_mapping(entries):
    global inputs
    outputs = set(inputs)

    for entry in entries:
        out_rstart, in_rstart, length = tuple([int(i) for i in entry.split()]) 
        in_rend = in_rstart + length # exclusive

        for r in set(inputs): # a copy is used so it will remain unaltered during iteration
            if r[0] >= in_rend or r[1] < in_rstart:
                continue

            # range intersects with current map entry
            # r[0]       in_rstart       in_rend       r[1]
            # --- r_prior ---|--- r_map ---|--- r_post ---
            inputs.remove(r)
            outputs.remove(r)

            # mapped range
            # assuming there are no conflicting mappings, 
            # no part of r_map will be mapped by any other entries
            # and is therefore safe to disclude from inputs
            shift = out_rstart - in_rstart
            r0 = max(r[0], in_rstart) # r may start after in_rstart
            r1 = min(r[1], in_rend) # r may end before in_rend
            r_map_out = (r0 + shift, r1 + shift)
            outputs.add(r_map_out)

            # unmapped ranges of r can still be mapped by other entries
            # therefore, should exist in inputs, 
            # they should be included in outputs in case they are not mapped

            # prior-range
            r_prior = (r[0], in_rstart)
            if r_prior[1] - r_prior[0] > 0:
                inputs.add(r_prior)
                outputs.add(r_prior)

            # post-range
            r_post = (in_rend, r[1])
            if r_post[1] - r_post[0] > 0:
                inputs.add(r_post)
                outputs.add(r_post)

    inputs = set(outputs)


# there are 7 mapping blocks, each separated by blank line
block_start = 3
lines.append('\n')
for _ in range(7):
    block_end = lines[block_start::].index('\n') + block_start
    block = lines[block_start:block_end]
    apply_mapping(block)
    block_start = block_end + 2

print(min(inputs)[0])

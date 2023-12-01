#!/usr/bin/env python3

sum = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        first = last = None
        for c in line:
            if not c.isdigit():
                continue
            if first is None:
                first = c
            last = c
        
        sum += int(first + last)

print(sum)

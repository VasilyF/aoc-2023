#! /usr/bin/env python3

res = 0

with open('input.txt') as f:
    for line in f.readlines():
        win_nums, *my_nums = line.split(':')[1].split('|')
        win_nums = set(win_nums.strip().split())
        my_nums = set(my_nums[0].strip().split())
        common = win_nums.intersection(my_nums)
        points = 2**(len(common) - 1) if len(common) else 0
        res += points 
    print(res)

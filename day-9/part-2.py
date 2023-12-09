#! /usr/bin/env python3

def all_zeros(it):
    for elem in it:
        if elem != 0:
            return False
    return True


def extrapolate(nums):
    if all_zeros(nums):
        return 0

    diffs = []
    for i in range(len(nums) - 1):
        diffs.append(nums[i+1] - nums[i])

    return nums[0] - extrapolate(diffs)


with open('input.txt') as f:
    lines = f.readlines()

res = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    res += extrapolate(nums) 

print(res)

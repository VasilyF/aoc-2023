#! /usr/bin/env python3

def common(line):
    win_nums, *my_nums = line.split(':')[1].split('|')
    win_nums = set(win_nums.strip().split())
    my_nums = set(my_nums[0].strip().split())
    return len(win_nums.intersection(my_nums))


with open('input.txt') as f:
    lines = f.readlines()
    num_cards = [1]*len(lines)
    for card, line in enumerate(lines):
        for j in range(1, common(line) + 1):
            num_cards[card + j] += num_cards[card]

    print(sum(num_cards))

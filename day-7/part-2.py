#! /usr/bin/env python3
from functools import total_ordering
from collections import defaultdict


class Type:
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OAK = 4
    FULL_HOUSE = 5
    FOUR_OAK = 6
    FIVE_OAK = 7


@total_ordering
class Hand:
    ORDER = 'J23456789TQKA'
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        
        freq = defaultdict(int)
        for c in cards:
            freq[c] += 1

        if 'J' in freq:
            num_jokers = freq['J']
            if num_jokers < 5:
                del freq['J']
                max_key = max(freq, key=freq.get)
                freq[max_key] += num_jokers

        match len(freq):
            case 1:
                self.type = Type.FIVE_OAK
            case 2:
                if 4 in freq.values():
                    self.type = Type.FOUR_OAK
                else:
                    self.type = Type.FULL_HOUSE
            case 3:
                if 3 in freq.values():
                    self.type = Type.THREE_OAK
                else:
                    self.type = Type.TWO_PAIR
            case 4:
                self.type = Type.ONE_PAIR
            case 5:
                self.type = Type.HIGH_CARD


    def __repr__(self):
        return f'{self.cards}'


    def __lt__(self, other):
        if self.type == other.type:
            for i in range(5):
                if self.cards[i] == other.cards[i]:
                    continue
                else:
                    return Hand.ORDER.find(self.cards[i]) < Hand.ORDER.find(other.cards[i])
        return self.type < other.type
        

with open('input.txt') as f:
    lines = f.readlines()

hands = []
for line in lines:
    line = line.split()
    cards = line[0]
    bid = int(line[1])
    hands.append(Hand(cards, bid))

hands.sort()

res = 0
for i, hand in enumerate(hands):
    res += hand.bid*(i+1)

print(res)

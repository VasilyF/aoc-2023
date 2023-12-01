#!/usr/bin/env python3

digits_3 = {'one': '1', 'two': '2', 'six': '6', }
digits_4 = {'four': '4', 'five': '5', 'nine': '9'} 
digits_5 = {'three': '3', 'seven': '7', 'eight': '8'}
sum = 0

'''
returns digit (as char) starting at s[i] or None
'''
def get_digit(s, i):
    if s[i].isdigit(): return s[i]

    # 3 char digit
    if i + 3 > len(s):
        return 
    sub_str = s[i:i+3] 
    if sub_str in digits_3: return digits_3[sub_str]

    # 4 char digit
    if i + 4 > len(s):
        return 
    sub_str = s[i:i+4] 
    if sub_str in digits_4: return digits_4[sub_str]

    # 5 char digit
    if i + 5 > len(s):
        return 
    sub_str = s[i:i+5] 
    if sub_str in digits_5: return digits_5[sub_str]

    return
    

with open('input.txt', 'r') as f:
    for line in f.readlines():
        first = last = None
        for i in range(len(line)):
            digit = get_digit(line, i)
            if not digit:
                continue
            if first is None:
                first = digit
            last = digit

        sum += int(first + last)

print(sum)

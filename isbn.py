#!/bin/env python3

import sys

if len(sys.argv)<2:
    print("usage: %s <9_or_10_digit_number>" % sys.argv[0])
    exit(1)

def calc_isbn_suffix(n):
    code_sum = 0
    for i, digit in enumerate(n):
        code_sum += int(digit) * (10 - i)
    parity = (11 - code_sum % 11) % 11
    if parity < 10:
        suffix = str(parity)
    elif parity == 10:
        suffix = "X"
    return suffix

def isbn(n):
    if len(n)==9:
        try:
            int(n)
        except:
            return "error: input is not an integer."+"\tDon't use hyphens between digits"
        return n+calc_isbn_suffix(n)
    elif len(n)==10:
        try:
            int(n[:len(n)-1])
        except:
            return "error: input w/o parity suffix is not an integer"+"\tDon't use hyphens between digits"
        parity = n[-1]
        return calc_isbn_suffix(n[:len(n)-1]) == parity
    else:
        return "error: input is not 9 or 10"+"\tDon't use hyphens between digits"

print(isbn(sys.argv[1]))
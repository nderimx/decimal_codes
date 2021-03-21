#!/bin/env python3

import sys

if len(sys.argv)<2:
    print("usage: % <9-10digit_number>")
    exit(1)

# implement the exact spec. There might not be a "XI" suffix
def calc_isbn_suffix(n):
    code_sum = 0
    for i, digit in enumerate(n):
        code_sum += int(digit) * (10 - i)
    parity = 11 - code_sum % 11
    if parity < 10:
        suffix = str(parity)
    elif parity == 10:
        suffix = "X"
    elif parity == 11:
        suffix = "XI"
    return suffix

def isbn(n):
    if len(n)==9:
        try:
            int(n)
        except:
            return "error: input is not an integer"
        return n+calc_isbn_suffix(n)
    elif len(n)==10 or len(n)==11:
        sf = 2 if n[-1] == "I" else 1
        try:
            int(n[:len(n)-sf])
        except:
            return "error: input w/o parity suffix is not an integer"
        parity = n[-sf]
        return calc_isbn_suffix(n[:len(n)-sf]) == parity
    else:
        return "error: input is not 9 or 10"

print(isbn(sys.argv[1]))
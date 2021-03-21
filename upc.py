#!/bin/env python3

import sys

if len(sys.argv)<2:
    print("usage: % <11-12digit_number>")
    exit(1)

# implement the exact spec. This implementation allows "10" as a parity suffix
def calc_upc_suffix(n):
    code_sum = 0
    for i, digit in enumerate(n):
        if i%2==0:
            code_sum += int(digit) * 3
        else:
            code_sum += int(digit)
    parity = 10 - code_sum % 10
    return str(parity)

def upc(n):
    try:
        int(n)
    except:
        return "error: input is not an integer"
    if len(n)==11:
        return n+calc_upc_suffix(n)
    elif len(n)==12:
        suffix = n[-1]
        return suffix == calc_upc_suffix(n[:len(n)-1])
    else:
        return "error: input is not 9 or 10"

print(upc(sys.argv[1]))
#!/bin/python3

import sys

def calculate(x):
# Complete this function
    if x <= 1 or x >= 100:
        return 'number out of bounds'
    else:
        x = x%11
        return x

if __name__ == "__main__":
    x = int(input().strip())
    result = calculate(x)
    print(result)
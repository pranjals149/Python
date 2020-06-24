# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. 
# Print the decimal value of each fraction on a new line.

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    ne = 0
    z = 0
    for i in range(0, n):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0: 
            ne += 1
        elif arr[i] == 0:
            z += 1
        pr = p/n
        nr = ne/n
        zr = z/n
    print(round(pr, 6))
    print(round(nr, 6))
    print(round(zr, 6))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

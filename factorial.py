# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:17:04 2018

@author: Shilpi

Task 
Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

Sample Input

3
Sample Output

6

"""

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    print(result)

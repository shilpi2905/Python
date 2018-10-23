# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:38:15 2018

@author: Shilpi

Task 
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2

"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bin_n = bin(n)
    print(bin_n)
    bin_str = bin_n[2:]
    count = 0
    count_list = []
    for i in bin_str:
        if i == '1':
            count +=1
        else:
            count_list.append(count)
            count = 0
    count_list.append(count)
    print(max(count_list))
        

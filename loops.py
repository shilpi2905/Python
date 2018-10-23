# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 00:36:38 2018

@author: Shilpi
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        print(str(n) + " X " + str(i) + " =", (n*i))

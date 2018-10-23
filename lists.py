# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 00:46:34 2018

@author: Shilpi
"""

N = int(input())
myList = []
for i in range(0,N):
    i = input()
    myList.append(i)
    
for j in myList:
    j_eve = ""
    j_odd = ""
    for k in range(0, len(j)):
        if k%2 == 0:
            j_eve+=j[k]
        else:
            j_odd+=j[k]
    print(j_eve + " "+ j_odd)
        
    

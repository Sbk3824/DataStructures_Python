#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:40:16 2019

@author: sbk
"""

# First Non-Repeating Integer in a list

def findFirstUnique(lst):
    counts = {} # Creating a dictionary
    counts = counts.fromkeys(lst,0) # Initializing dictionary with pairs like (lst[i],0)
    for ele in lst:
        counts[ele]+=1 # Incrementing for every repitition 
    for ele in lst:
        if counts[ele] <= 1:
            return ele
    return None
  
print(findFirstUnique([ 1,1,1,2 ]))
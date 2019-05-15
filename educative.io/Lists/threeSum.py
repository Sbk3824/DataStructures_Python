#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:33:12 2019

@author: sbk
"""

def findSum(lst,value):
  #lst.sort()
  i, j = 0, len(lst) -1
  
  while (i <= j):
    sum = lst[i] + lst[j]
    if sum < value:
      i += 1
    elif sum > value:
      j -= 1
    else:
      return True
  return False

def three_sum(A,value):
    A.sort()
    return any(findSum(A, value - a) for a in A)
    

print(findSum([1,2,3,4,7,8],16))
#print(three_sum([1,2,3,4,7,8],24))
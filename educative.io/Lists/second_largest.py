#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:51:27 2019

@author: sbk
"""

def findSecondMaximum(lst):
  if (len(lst) < 2):
    return

  first = second = float('-inf') # Negative infinite number
  for i in range(len(lst)): 
    if (lst[i] > first): 
      second, first = first, lst[i] 
    elif (lst[i] > second and lst[i] != first):
      second = lst[i]
      
  if (second == float('-inf')): 
      return 
  else: 
      return second 

print(findSecondMaximum([9,2,3,9,6]))
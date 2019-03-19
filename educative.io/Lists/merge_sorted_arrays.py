#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:05:52 2019

@author: sbk
"""

def mergeArrays(lst1,lst2):
  # Write your code here
  
  if not lst1 and not lst2:
    return False
  if not lst1:
    return lst2
  if not lst2:
    return lst1

  i, j = 0, 0
  while i < len(lst1) and j < len(lst2):
    if lst1[i] > lst2[j]:
      lst1.insert(i, lst2[j])
      i += 1
      j += 1
    else:
      i += 1
      
  if j < len(lst2):
    lst1.extend(lst2[j:])
  return lst1


s1 = [1,3,5,6,8,10]
s2 = [4,8,12]
mergeArrays(s1,s2)


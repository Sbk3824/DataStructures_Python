#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:28:41 2019

@author: sbk
"""
"""

# Using Dictionaries

def findSum(lst,value):
  foundValues = {}
  for ele in lst:
    try:
      foundValues[value - ele]
      return [value - ele, ele]
    except:
      foundValues[ele] = 0
  return False
"""

# Using Sets

def findSum(lst,value):
  foundValues = set()
  for ele in lst:
    if value - ele in foundValues:
        return [value - ele, ele]
    foundValues.add(ele)
  return False

print(findSum([1,3,2,4],6))